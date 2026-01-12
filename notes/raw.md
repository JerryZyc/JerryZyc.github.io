                                        Spatially-Enhanced Recurrent Memory for Long-Range
                                        Mapless Navigation via End-to-End Reinforcement Learning
                                        Fan Yang1 , Per Frivik1 , David Hoeller1 , Chen Wang2 , Cesar Cadena1 , and Marco Hutter1



                                        Abstract
                                        Recent advancements in robot navigation, particularly with end-to-end learning approaches such as reinforcement
                                        learning (RL), have demonstrated remarkable efficiency and effectiveness. However, successful navigation still depends
                                        on two key capabilities: mapping and planning, whether implemented explicitly or implicitly. Classical approaches rely
                                        on explicit mapping pipelines to transform and register egocentric observations into a coherent map for the planning
                                        module. In contrast, end-to-end learning often achieves this implicitly—through recurrent neural networks (RNNs) that
                                        fuse current and historical observations into a latent space for planning. While existing architectures, such as LSTM
                                        and GRU, can capture temporal dependencies, our findings reveal a critical limitation: their inability to effectively
arXiv:2506.05997v2 [cs.RO] 4 Sep 2025




                                        perform spatial memorization. This capability is essential for transforming and integrating sequential observations
                                        from varying perspectives to build spatial representations that support planning tasks. To address this, we propose
                                        Spatially-Enhanced Recurrent Units (SRUs)—a simple yet effective modification to existing RNNs—that enhance
                                        spatial memorization. To improve navigation performance, we introduce an attention-based network architecture
                                        integrated with SRUs, enabling long-range mapless navigation using a single forward-facing stereo camera. Additionally,
                                        we employ regularization techniques to facilitate robust end-to-end recurrent training via RL. Experimental results
                                        demonstrate that our approach improves long-range navigation performance by 23.5% overall compared to existing
                                        RNNs. Furthermore, when equipped with SRU memory, our method outperforms both RL baseline approaches—one
                                        relying on explicit mapping and the other on stacked historical observations—achieving overall improvements of 29.6%
                                        and 105.0%, respectively, in diverse environments that require long-horizon mapping and memorization capabilities.
                                        Finally, we address the sim-to-real gap by leveraging large-scale pretraining on synthetic depth data, enabling zero-
                                        shot transfer for deployment across diverse and complex real-world environments.


                                        Keywords
                                        Spatial Memory, End-to-End Mapless Navigation, Recurrent Neural Networks, Reinforcement Learning



                                        1   Introduction                                                 approaches are not easily deployable on smaller robotic
                                                                                                         platforms and often struggle to generalize to environments
                                        End-to-end learning for robot navigation has recently gained     beyond structured road networks. In contrast, embedded
                                        significant attention with its potential to address two major    robots often rely on end-to-end learning approaches, either
                                        challenges inherent in classical modular approaches: (a)         by imitating behaviors from datasets (Shah et al. 2023;
                                        system delays and (b) the difficulty of modeling complex         Karnan et al. 2022; Cèsar-Tondreau et al. 2021; Loquercio
                                        kinodynamic environmental interactions. These challenges         et al. 2021) or by optimizing policies through reinforcement
                                        have traditionally hindered the development of high-             learning (RL) (Wijmans et al. 2019; Zhu et al. 2017; Sur-
                                        speed platforms with intricate dynamics, such as legged-         mann et al. 2020). These methods typically employ specific
                                        wheeled robots. However, end-to-end learning approaches          network architectures, such as recurrent neural networks
                                        face their own challenges, particularly in achieving efficient   (RNNs), to implicitly learn spatial-temporal mappings (Wij-
                                        spatial mapping. Unlike classical mapping pipelines, which       mans et al. 2019, 2023). While these approaches have
                                        explicitly transform historical ego-centric observations into    demonstrated success in structured indoor environments with
                                        a coherent map frame for downstream planning, end-to-end         discretized action and observation spaces, their performance
                                        learning relies on neural networks to implicitly learn this      often diminishes in more complex, real-world scenarios that
                                        process. This requires the network to iteratively build and      involve continuous action spaces and dynamic motions.
                                        update an environmental representation of the surroundings          Recently, for real-world deployments, researchers have
                                        and understand the spatial-temporal relationships between        started integrating explicit mapping pipelines (Miki et al.
                                        observations.                                                    2022b) to fuse ego-centric observations and provide
                                           In autonomous driving, large-scale mapping mod-               environmental information to learning modules for tasks
                                        ules (Mohajerin and Rohani 2019; Mescheder et al. 2019;
                                        Wei et al. 2023; Wang et al. 2025) are trained on thou-
                                                                                                         1 Robotic Systems Lab, ETH Zurich, Zurich, Switzerland
                                        sands of hours of data, enabling robust spatial mapping
                                                                                                         2 Spatial AI & Robotics Lab, University at Buffalo, Buffalo, NY, USA
                                        with specifically designed architectures, such as occu-
                                        pancy networks (Mescheder et al. 2019) or occupancy              Corresponding author:
                                        grid maps (Mohajerin and Rohani 2019). However, such             Fan Yang, fanyang1@ethz.ch
2                                                                                                                             ()


such as perceptive locomotion (Miki et al. 2022a) and            regularizations during end-to-end RL training is crucial.
navigation (Lee et al. 2024; Francis et al. 2020; Weerakoon      Furthermore, to address the sim-to-real gap caused by noisy
et al. 2022). This raises an important question: can end-to-     depth images, we pretrain the image encoder on a large-
end learning networks with implicit memory mechanisms,           scale synthetic dataset and augment the data using a fully
such as RNNs, match or surpass the performance of                parallelized depth-noise model, adapted from Handa et al.
approaches that rely on explicit mapping pipelines?              (2014a); Barron and Malik (2013a); Bohg et al. (2014a). In
Specifically, do RNNs have inherent limitations in learning      summary, our main contributions are as follows:
spatial-temporal mappings?
                                                                     • Addressing Spatial Mapping Limitations with
   While RNNs excel at capturing temporal dependencies,
                                                                       SRUs: We identify that standard RNNs, while effec-
showcased by their success in various sequential tasks,
                                                                       tive in capturing temporal dependencies, can strug-
such as natural language processing (Sutskever et al.
                                                                       gle with spatial registration of observations from
2014) and time-series prediction (Siami-Namini et al.
                                                                       different perspectives. To overcome this, we intro-
2019), their ability to learn spatial transformations and
                                                                       duce Spatially-Enhanced Recurrent Units (SRUs) that
memorization remains a topic of research. RNNs are
                                                                       enhance the ability to learn implicit spatial transforma-
designed to process sequences of data by maintaining an
                                                                       tions from sequences of ego-centric observations.
internal state that captures temporal dependencies. However,
                                                                     • End-to-End Reinforcement Learning with SRUs
it is not yet clear to what extent they can effectively
                                                                       and Attention-based Policy: We integrate the SRU
learn spatial transformations and integrate observations from
                                                                       unit into a proposed attention-based network archi-
different perspectives. Classical approaches achieve spatial
                                                                       tecture, enabling improved end-to-end reinforcement
registration through homogeneous transformations in three-
                                                                       learning for long-range mapless navigation tasks using
dimensional space, aligning observations into a consistent
                                                                       only ego-centric observations.
local or global frame. For RNNs to achieve effective spatial
                                                                     • Large-Scale Pretraining for Zero-Shot Sim-to-Real
registration, they must not only memorize sequences but also
                                                                       Transfer in Long-Range Mapless Navigation: By
learn to transform and integrate observations across time and
                                                                       leveraging large-scale synthetic pretraining and a
space.
                                                                       parallelizable depth-noise model, our system bridges
   In this work, we examine the spatial-temporal mem-
                                                                       the sim-to-real gap, enabling zero-shot deployment
ory capabilities of several recurrent architectures, including
                                                                       on a legged-wheel platform in diverse real-world
Long Short-Term Memory (LSTM) (Hochreiter and Schmid-
                                                                       environments, using a single forward-facing stereo
huber 1997), Gated Recurrent Unit (GRU) (Cho et al. 2014),
                                                                       camera for long-range mapless navigation.
and recent State-Space Models (SSMs) such as S4 (Gu
et al. 2021) and Mamba-SSM (Gu and Dao 2023). We
evaluate these models on two criteria: (i) their ability to      2   Related Works
memorize temporal sequences and (ii) their capacity to           The navigation and planning problem has been studied
register and transform sequential observations across varying    extensively for decades. Early approaches relied on classic
spatial perspectives. Our findings indicate that, while these    search-based methods, including Dijkstra’s algorithm and
models perform well in capturing temporal dependencies,          A* (Dijkstra 1959; Hart et al. 1968) operating on pre-
they exhibit limitations in spatial registration, particularly   discretized grids, as well as on sample-based techniques
under conditions of dynamic ego-motion and rapidly chang-        such as the Rapidly-exploring Random Tree (RRT) fam-
ing perspectives.                                                ily—including variants like RRT*, RRT-Connect (LaValle
   To address this limitation, we introduce Spatially-           et al. 2001; Karaman and Frazzoli 2011; Kuffner and LaValle
Enhanced Recurrent Units (SRUs), a simple yet effective          2000), etc.—and probabilistic roadmap (PRM) methods,
modification to standard LSTM and GRU units that enhances        such as Lazy PRM and SPARS (Kavraki et al. 1996; Bohlin
their spatial registration capabilities when processing          and Kavraki 2000; Dobson and Bekris 2014). While these
sequences of ego-centric observations. Unlike classical          techniques have achieved significant success in robotics and
mapping pipelines that rely on explicit homogeneous              real-world applications (Wellhausen and Hutter 2023), they
transformations, our approach enables the recurrent units to     depend on building or the existence of a predefined naviga-
implicitly learn the transformations from varying observation    tion or occupancy map. Consequently, they often struggle
perspectives effectively. To further enhance the performance     in unknown or dynamic environments (Yang et al. 2022a),
of long-range navigation tasks, we propose an attention-         particularly when planning under static-world assumptions
based network architecture integrated with SRUs, allowing        or when complex kinodynamic constraints are present (Webb
the model to learn long-range mapless navigation policies        and Berg 2012; Ortiz-Haro et al. 2024). Moreover, these
using only ego-centric observations via end-to-end RL. Our       classical methods typically require an additional perception
experiments demonstrate improvements in spatial awareness        and mapping module, and the predetermined traversability or
compared to the baselines. With the SRU memory, the              occupancy maps are usually based on heuristic designs rather
implicit recurrent approach via RL with sparse rewards           than being optimized for a specific robotic platform.
promotes robust exploration in complex 3D and maze-                 To address these limitations, recent research has increas-
like environments, outperforming the baseline that rely on       ingly turned to learning-based approaches, especially for
explicit mapping and memory modules.                             more complex robotic agents (e.g., quadrupeds or wheel-
   To prevent premature convergence to suboptimal strategies     legged systems). For instance, recent works in imitation
and fully exploit the capabilities of the proposed attention-    learning leverage large-scale video data or demonstra-
based recurrent structure, we find that incorporating            tions (Pfeiffer et al. 2017; Bojarski et al. 2016; Loquercio


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                3


et al. 2021; Shah et al. 2022, 2023) to directly map raw         region G ⊂ R3 , such that the relative goal position satisfies
egocentric sensory inputs to navigation actions. Given the       ∥pt ∥ < ϵ, where ϵ > 0 represents a specified tolerance,
challenges of capturing dynamic, closed-loop interactions        within a finite time horizon t ≤ Tmax . The robot follows
from purely offline data, researchers have also explored         a policy π that maps its current state st to an action
model-free reinforcement learning (RL) methods (Shi et al.       at . However, due to the egocentric setup, the agent’s
2019; Wijmans et al. 2019; Choi et al. 2019; Hoeller et al.      current state st is not fully observable from a single sensor
2021; Truong et al. 2021; Wu et al. 2021; Ruiz-Serra et al.      snapshot. Formally, we model the navigation task as a
2022; Fu et al. 2022; Huang et al. 2023; Bhattacharya et al.     Partially Observable Markov Decision Process (POMDP),
2024; Lee et al. 2024) that train navigation policies end-to-    characterized by the tuple:
end by simulating the entire robot dynamics. By replacing
the traditional perception, mapping, and planning pipeline                            (S, A, T , R, O, Z, γ),
with a tailored network—such as architectures based on
recurrent networks (Wijmans et al. 2019; Choi et al. 2019;       with the following components:
Hoeller et al. 2021; Wu et al. 2021) or Transformers with              • S: the set of all possible states of the environment.
attention mechanisms (Ruiz-Serra et al. 2022; Huang et al.             • A: the set of actions available to the robot.
2023; Bhattacharya et al. 2024; Zeng et al. 2024)—these                • T : S × A × S → [0, 1]: the state transition function,
approaches have achieved improvements in navigation tasks                where T (s, a, s′ ) denotes the probability of transition-
as well as in robotic locomotion (Miki et al. 2022a; Yang                ing from state s to state s′ when action a is taken.
et al. 2022b; Kareer et al. 2023).                                     • R : S × A → R: the reward function, assigning a
   A key challenge with end-to-end approaches is learning                scalar reward to each state-action pair.
a robust state representation from the partial observations            • O: the set of all possible observations.
provided by egocentric sensors. Recent studies have                    • Z : S × A × O → [0, 1]: the observation function,
attempted to mitigate this challenge by incorporating explicit           specifying the probability of receiving an observation
mapping and memory mechanisms (Savinov et al. 2018;                      given the current state and action.
Cimurs et al. 2021; Fu et al. 2022; Lee et al. 2024)                   • γ ∈ [0, 1]: the discount factor that balances immediate
or by employing specialized network architectures like                   reward and future payoffs.
RNNs (Hoeller et al. 2021; Wijmans et al. 2019; Choi
et al. 2019). However, RNNs—originally designed to capture       The action at ∈ A is executed in the robot’s local frame at
temporal sequences in language tasks (Cho et al. 2014)—are       time t. At each time step t, the robot receives an observation
not inherently well-suited for spatial mapping, particularly     ot ∈ O and combines it with its historical observations Ht−1
when processing sequential egocentric observations from          to determine the current state, where Ht−1 is defined as:
continuously changing perspectives. For instance, while
prior studies in indoor navigation have shown that spatial                         Ht−1 := {o1 , o2 , . . . , ot−1 }.
cues can be decoded from RNN memories, this effect is
limited to employing binary contact sensing and does not         We define a function f that fuses current and historical
extend to high-dimensional visual inputs (Wijmans et al.         observations into an estimate ŝt of the unobservable state
2023). Moreover, recent findings suggest that variations in      st ∈ S:
recurrent network architectures have minimal impact on                               ŝt = f (ot , Ht−1 ).
the final task-level rewards achieved through reinforcement      The policy π then maps the estimated state ŝt to an action at :
learning (Duarte et al. 2023). This indicates that, despite
architectural differences, some fundamental limitations may                                  at = π(ŝt ).
persist across these RNN units.
   In this paper, we explore a key limitation of existing RNN-   Due to the robot’s ego-motion, the current observation
based architectures in addressing partial observability—their    ot can be captured from a different perspective or
spatial memorization capabilities—highlighting their short-      observation frame compared to historical observations
comings in learning spatial transformations and integrating      in Ht−1 . Therefore, to fuse observations from different
observations from different perspectives. We then introduce      viewpoints, the function f typically involves a spatial
Spatially-Enhanced Recurrent Units (SRUs) and demon-             transformation that aligns the observations into a coherent
strate their effectiveness in improving long-range mapless       reference frame to estimate the current state st for the policy
navigation tasks with a specifically designed attention-based    π. In classical mapping pipelines, spatial transformations
network structure via end-to-end reinforcement learning.         are typically achieved through homogeneous transformations
                                                                 that combine rotations and translations. However, in end-
                                                                 to-end learning approaches, the function f , which can
3     Problem Statement                                          be parameterized by neural network weights, is learned
Consider a robot operating in a three-dimensional (3D)           implicitly.
environment E ⊂ R3 . At each time step t, the robot is
located at a configuration defined by its position and           4     Methodology
orientation in SE(3), and receives an observation ot through
its egocentric sensors. The navigation objective is defined      4.1     Overview
as starting from an initial relative goal position p1 ∈ R3 in    To tackle the long-range navigation task, we first examine
the robot’s egocentric frame and reaching a designated goal      and demonstrate the limitations of existing recurrent


Prepared using sagej.cls
4                                                                                                                                  ()


architectures (e.g., LSTM, GRU, S4, and Mamba-SSM)                   and h̃t are the update, reset, and candidate hidden states in
in a spatial-temporal memory task. We then introduce                 GRU, respectively. The weights W and biases b are learnable
the Spatially-Enhanced Recurrent Units (SRUs). Next,                 parameters, and σ denotes the sigmoid activation function.
we integrate SRUs into an attention-based network                    Note that for all the letters used in the RNN formulations,
architecture to learn long-range mapless navigation via end-         we use a “monospaced” font style to prevent confusion with
to-end reinforcement learning. Furthermore, we discuss the           the symbols used in the remainder of the paper.
importance of incorporating regularization techniques to                More recently, the State-Space Model (Gu et al. 2021) was
prevent early overfitting, which we find to be crucial to            introduced, which is inspired by the general form of state
enhance SRUs’ spatial memorization. Finally, we address              space models widely used in control theory. Such models
the sim-to-real gap by pretraining the depth image encoder           take the following form in discrete time:
on large-scale synthetic depth data and incorporating a
parallelizable depth-noise model, enabling zero-shot transfer                             xt = Ā xt−1 + B̄ ut ,
to real-world environments.                                                               yt = C̄ xt + D̄ ut ,
                                                                     where xt represents the state at time t, ut the input, and yt
4.2      Background: Recurrent Neural Networks
                                                                     the output. The matrices Ā, B̄, C̄, and D̄ define the system
Recurrent Neural Networks (RNNs) are a class of neural               dynamics.
networks designed to process sequential data by maintaining             In Gu et al. (2020a), a so-called HiPPO matrix is proposed
a hidden state that captures temporal dependencies. Given a          for Ā and B̄ to optimally project historical information into
sequence of inputs x := (x1 , x2 , . . . , xT ), an RNN computes     the current state via a polynomial basis. Although this
a sequence of hidden states h := (h1 , h2 , . . . , hT ) using the   approach has led to a new family of RNN models (e.g., S4,
following recursive formula:                                         S5, Mamba-SSM) that excel at capturing long-term temporal
                                                                     dependencies, their emphasis on long temporal processing is
                           ht := f (xt , ht−1 ),                     not the focus of this paper; therefore, we omit further details
                                                                     on these models.
where f is a function that combines the previous hidden
state ht−1 with the current input xt to compute the current
hidden state ht . This is analogous to the function mentioned
                                                                     4.3    Spatial Mapping Limitations in RNNs
earlier, which fuses the current observation ot with the             Achieving long-range mapless navigation from ego-centric
historical observations Ht−1 into the estimated current state        observations requires the robot to perform effective spatial
ŝt . The hidden state ht captures the network’s internal            mapping. In three-dimensional (3D) space, spatial mapping
representation at time t, encoding information from the              is commonly achieved using homogeneous transformations,
entire input sequence up to that point. However, the vanilla         which combine rotations and translations. A general
version of RNN can suffer from gradient vanishing and                representation of such a transformation is expressed as:
explosion issues (Hochreiter and Schmidhuber 1997; Cho                                   ′            
                                                                                         p        R t p
et al. 2014). To address these problems, several variants have                               = ⊤               ,
                                                                                         1        0    1 1
been proposed, including LSTM and GRU, as commonly
used in sequential tasks nowadays. These models introduce            where p and p′ are the coordinates of a point in the original
gating mechanisms that control the flow of information               and transformed frames, R is the rotation matrix, and t is
through the network, enabling better long-term memory                the translation vector. In the context of RNNs, this spatial
retention and gradient flow. Those types of RNNs adopted             mapping and transformation is implicitly learned through the
gates and residual connections across temporal sequences,            function f , which integrates the current observation ot with
resulting in strong performance in various sequential tasks.         the historical observations Ht−1 to estimate the current state
The standard LSTM unit takes the following form:                     st .
                                                                         In this section, we assess the spatial and temporal map-
                it = σ(Wxi xt + Whi ht−1 + bi ),
                                                                     ping performance of existing recurrent structures—namely
                ft = σ(Wxf xt + Whf ht−1 + bf ),                     LSTM, GRU, and the recent S4 and Mamba-SSM—on two
                ot = σ(Wxo xt + Who ht−1 + bo ),                     fronts: (i) temporal memorization and (ii) spatial transfor-
                gt = tanh(Wxg xt + Whg ht−1 + bg ),                  mation and memorization. Consider an abstract scenario
                                                                     relevant to the navigation task, in which a robot is initialized
                ct = ft ⊙ ct−1 + it ⊙ gt ,
                                                                     at a pose in SE(3) and moves randomly within the three-
                ht = ot ⊙ tanh(ct ),                                 dimensional environment E ⊂ R3 . At each time step t, the
                                                                     robot receives an observation ot containing the coordinates
and the GRU unit:
                                                                     of observed landmarks lti ∈ R3 , defined relative to the robot’s
                                                                     current frame (indicated by the subscript t). Each landmark
                                       
          zt = σ Wxz xt + Whz ht−1 + bz ,
                                                                    is also associated with a binary categorical label ci , which
          rt = σ Wxr xt + Whr ht−1 + br ,
                                                                    is temporally relevant and independent of the observation
          h̃t = tanh Wxh xt + Whh (rt ⊙ ht−1 ) + bh ,                frame. Additionally, the robot is provided with its ego-
          ht = (1 − zt ) ⊙ h̃t + zt ⊙ ht−1 ,                         motion transformation matrix Mtt−1 , representing the trans-
                                                                     formation from the previous pose at time step t − 1 to the
where it , ft , ot , and gt are the input, forget, output, and       pose at time step t. This transformation enables the network
cell gate activations in LSTM, respectively. Similarly, zt , rt ,    to align and integrate observations into a unified reference


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                5




                           (a) Temporal Training Loss




                                                                                    (a) Spatial Mapping with LSTM




                            (b) Spatial Training Loss


Figure 1. Training for the Spatial-temporal Memorization: (a)
Temporal memorization loss shows that standard RNN units
(LSTM, GRU, S4, and Mamba-SSM) effectively recall sequential
information. (b) Spatial memorization loss indicates that these
units struggle with accurate spatial transformations and
memorization under changing observation perspectives,
resulting in misaligned landmark coordinates.                                    (b) Spatial Mapping with SRU-LSTM




frame, akin to classical homogeneous transformations. Over
a sequence of T time steps, the RNN processes these
observations. At the final step T , the network is evaluated
simultaneously on its ability to:


     • Memorize and accurately predict the sequence of
       binary categorical labels associated with the observed
       landmarks, ensuring temporal association and order                              (c) Spatial Memory Error
       preservation (Temporal Task).
     • Transform and register the spatial coordinates of all      Figure 2. Spatial Mapping Comparison: (a) and (b) depict the
       observed landmarks into the final robot frame at t =       spatial mapping performance of LSTM and SRU-LSTM units on
       T , achieving spatial alignment and memorization of        synthetic data, respectively, as the robot follows a spiral path,
                                                                  observing landmarks from different perspectives. At the end of
       their positions (Spatial Task).
                                                                  the path, the robot is tasked with memorizing and transforming
                                                                  the observed landmark coordinates into the final robot frame.
                                                                  Numbers indicate observation time steps. (c) illustrates the
The training details are provided in Appendix A. The              mean spatial memory errors (log scale) across observation step
results indicate that while LSTM, GRU, S4, and Mamba-             indices, ordered from the final (15) to the initial step (1),
SSM effectively encode temporal sequences and retain              averaged over various randomly generated trajectories and
landmark categories, as shown in Figure 1(a), they                observations.
face significant challenges in accurately memorizing
and transforming landmark coordinates from sequential
ego-centric observations. This limitation is reflected in
the higher mean squared error (MSE) when recalling                4.4    Spatially-Enhanced Recurrent Unit (SRU)
observed landmark positions during training, as depicted in       To address the limitations of spatial mapping of existing
Figure 1(b).                                                      RNN units, we propose a modification to the standard LSTM


Prepared using sagej.cls
6                                                                                                                                 ()


and GRU architectures by introducing an additional spatial          landmark coordinates into the final frame, as well as recalling
transformation operation. This enhancement results in a             the associated categories of the observed landmarks. Our
new class of units, termed Spatially-Enhanced Recurrent             experiments demonstrate that the SRU modification enables
Units (SRUs). The added operation enables the network               the network to effectively learn spatial transformations. In
to implicitly learn spatial transformations, aligning and           contrast, the baseline models struggle to align and memorize
memorizing observations from varying perspectives while             landmark coordinates observed in earlier steps, resulting in
preserving robust temporal memorization capabilities.               higher spatial errors, particularly for earlier observations, as
   The effectiveness of this approach is demonstrated               depicted in Figure 2(c). However, both SRU and baseline
by the training results of the spatial mapping task                 models achieve 100% accuracy in recalling the categories
mentioned above and illustrated in Figure 1. With the               of the observed landmarks. Since the temporal task results
SRU modification, the network effectively transforms and            are identical across all models, they are not visualized
memorizes observed landmark coordinates from different              Specifically in Figure 2. Furthermore, the latest recurrent
perspectives, as indicated by the spatial loss curve in             units, such as S4 and Mamba-SSM, which excel at long-
Figure 1(b), while preserving similar temporal memorization         term temporal memorization, exhibit even worse spatial
performance compared to standard LSTM and GRU units, as             memorization capabilities, as shown in both Figure 1(b) and
shown in Figure 1(a). The design of SRUs emerged through            Figure 2(c). The SRUs exhibit consistently low spatial errors
iterative experimentation and analysis of spatial mapping           across all observation steps, underscoring their superior
performance. The final formulation draws inspiration from           spatial memorization capabilities.
the multiplicative form of homogeneous transformations and
recent research on the use of the ”star operation” (element-        4.5     Attention-Based Recurrent Network
wise multiplication) to enhance the representational capacity               Architecture for Navigation
of neural networks (Ma et al. 2024).
   The following equations detail the modifications to              To leverage the SRUs in the navigation context, we propose
incorporate spatial transformations into both LSTM and              an attention-based recurrent network architecture for long-
GRU units, ensuring a balance between spatial memorization          range mapless navigation tasks using raw front-facing stereo
and temporal dependency learning. In each case, we compute          depth input, as illustrated in Figure 3. The network consists
an additional spatial transformation term, denoted as st ,          of a pretrained depth image encoder, two spatial attention
which acts as a mechanism to implicitly transform and align         layers incorporating both self-attention and cross-attention
the candidate state with the current observation’s perspective.     mechanisms to enhance and compress the encoded visual
For the modified LSTM, referred to as SRU-LSTM, we                  features, and a recurrent unit (SRU) that learns a spatial-
define:                                                             temporal representation of the state by fusing the current
                                                                    observation with historical observations. Finally, a multilayer
          st = Wxs xt + bs ,                                        perceptron (MLP) head computes the actions from the
                                              
          gt = tanh st ⊙ Wxg xt + Whg ht−1 + bg .                   recurrent hidden state, outputting velocity commands for the
                                                                    robot’s locomotion controller.
Similarly, for the modified GRU, referred to as SRU-GRU,            Depth Encoder Pretraining and Simulated Perception
the formulation is enhanced as follows:                             Noise For the depth encoder, we adopt a convolutional neu-
     st = Wxs xt + bs ,                                             ral network (CNN) backbone based on RegNet (Radosavovic
                                                                 et al. 2020), chosen for its simplicity and efficiency.
     h̃t = tanh st ⊙ Wxh xt + Whh (rt ⊙ ht−1 ) + bh .               This is further enhanced with a Feature Pyramid Net-
                                                                    work (FPN) (Lin et al. 2017) to capture spatial features
To further enhance spatial-temporal memorization, we                across multiple scales. The encoder is pretrained for self-
extend the SRU-LSTM with a refined gating mechanism (Gu             reconstruction on large-scale synthetic depth image data
et al. 2020b), simply referred to as SRU-Ours in the                from TartanAir (Wang et al. 2020) using a variational
following sections. This mechanism introduces an additional         autoencoder (VAE) framework. This pretraining enables the
refining function to address gating saturation issues during        encoder to learn and extract robust and generalizable fea-
recurrent training. The final modification, compared to the         tures from depth images, facilitating effective downstream
vanilla LSTM unit, is as follows:                                   navigation learning and deployment. However, depth images
         st = Wxs xt + bs ,                                         captured in simulation often differ from those obtained
                                                                 in real-world environments due to various sensor artifacts
         gt = tanh st ⊙ Wxg xt + Whg ht−1 + bg ,                    and noise. To address this sim-to-real gap, we integrate a
                                                                  parallelized depth-noise model, adapted from (Handa et al.
         rt = it ⊙ 1 − (1 − ft )2 + (1 − it ) ⊙ f2t ,               2014b; Barron and Malik 2013b; Bohg et al. 2014b), which
         ct = rt ⊙ ct−1 + (1 − rt ) ⊙ gt .                          introduces configurable noise to the depth images, such as:

The effectiveness of SRU is further validated and compared                • Edge Noise: Distortions at sharp depth discontinuities
to the standard LSTM unit in the designed spatial mapping                   due to abrupt changes in the scene.
task, as illustrated in Figure 2. In this task, the robot follows         • Filling Noise: Blurring artifacts introduced during the
a spiral path, observing landmarks from varying perspectives                interpolation of missing or unregistered pixels.
along its trajectory. At the end of the path, the robot                   • Rounding Noise: Quantization effects resulting from
is tasked with memorizing and transforming the observed                     sensor resolution limitations, causing rounding errors.


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                    7




Figure 3. Attention-based recurrent network architecture for navigation: The network integrates a pretrained image encoder and an
attention mechanism to compress and emphasize relevant features from encoded observations. These features, combined with
proprioceptive inputs, are processed by the SRU unit, which learns spatial transformations and temporal dependencies and fuses
them with historical observations to estimate the robot’s state. The state is then mapped to actions using an MLP-based head
integrated with the temporally consistent (TC) dropout layer for improved robustness and generalization.




                                                                      features while suppressing less important ones. Next, Ft′
                                                                      is processed by a cross-attention layer, where the query
                                                                      is derived from the robot’s egocentric proprioceptive state
                                                                      oprop
                                                                        t —which includes linear velocity vt , angular velocity
                                                                      ωt , projected gravity nt , and the previous action at−1 —as
                                                                      well as the current relative goal position pt . This procedure
                                                                      is illustrated in Figure 3. This operation compresses the
     (a) Original Synthetic Image   (b) Image with Artificial Noise
                                                                      2-dimensional feature map into a 1-dimensional latent
                                                                      representation
Figure 4. Simulated stereo depth noise: (a) Synthetic depth                                    F̂t ∈ RC×1 ,
image from the TartanAir dataset (Wang et al. 2020), (b) Image
with augmented artificial noise. The depth-noise model
                                                                      which preserves the most relevant spatial features while
introduces edge, filling, and rounding noise to the depth images,     reducing the dimensionality. This compressed feature F̂t is
simulating realistic sensor artifacts.                                then concatenated with the proprioceptive state oprop    t   and
                                                                      the relative goal position pt before being passed to the
                                                                      recurrent memory unit. There, it is fused with historical
                                                                      observations to form a spatial-temporal representation of
Figure 4 illustrates an example of the simulated stereo depth         the robot’s current state, integrating both exteroceptive and
noise. The depth-noise model is designed for efficient batch          proprioceptive information.
processing, enabling parallelized pretraining on large-scale             Figure 5 visualizes the output attention weights of the
datasets and during RL with simulated depth images. For               cross-attention layer across four distinct attention heads
implementation details, refer to Appendix B.                          (depicted in different colors), overlaid on the depth input.
Attention Layers for Feature Compression During nav-                  It highlights how the attention mechanism focuses on depth
igation, humans and animals tend to focus on the most                 features relevant to the robot’s current state. When the robot’s
relevant spatial cues rather than attempting to memorize              movement direction is manually altered, the output attention
all available information (Matthis et al. 2018). This selec-          weights shift accordingly, emphasizing spatial regions and
tive attention enables more efficient and effective memory            obstacles in the new direction. These behaviors emerge
usage. To emulate this, we combine self-attention and cross-          naturally during end-to-end learning, demonstrating the
attention mechanisms in our architecture. These spatial atten-        policy’s ability to effectively acquire critical spatial cues for
tion layers process high-dimensional visual inputs, extracting        navigation.
the information most relevant to the robot’s current state.
                                                                      Spatially-Enhanced Recurrent Unit (SRU) The Spatially-
Specifically, given the feature map encoded by the pretrained
                                                                      Enhanced Recurrent Unit (SRU), as described in Sec. 4.4,
depth encoder:
                                                                      processes the compressed feature map F̂t , along with
                       Ft ∈ RC×H×W ,
                                                                      the robot’s current proprioceptive state opropt     and the
each spatial feature Ftij (where i ∈ {1, . . . , H} and j ∈           previous hidden state ht−1 , to generate a spatial-temporal
{1, . . . , W }) is enriched with global context via a self-          representation of the surrounding environment from the
attention mechanism, resulting in a refined feature map               robot’s egocentric observations. The observation of the
Ft′ . Here, H and W denote the height and width of the                current proprioceptive state oprop
                                                                                                     t    provides essential ego-
feature map, respectively, while C represents the number              motion information, equivalent to the transformation matrix
of channels. The self-attention mechanism computes the                Mtt−1 in Sec. 4.3. The SRU learns to implicitly perform
attention weights across the spatial dimensions of the feature        spatial transformations, aligning the current observation
map, enabling the network to fuse and emphasize relevant              feature map F̂t with the previous hidden state ht−1 . The


Prepared using sagej.cls
8                                                                                                                                      ()




            (a) Robot State — Turning Left           (b) Robot State — Going Straight             (c) Robot State — Turning Right


Figure 5. Visualization of cross-attention weights corresponding to different robot states over raw real-world depth input: (a) When
the robot turns left, the attention weights highlight the left region, focusing on the left pillar in the depth image; (b) When the robot
moves straight, the attention weights emphasize the central region, capturing both pillars; (c) When the robot turns right, the
attention weights focus on the right region, concentrating on the right pillar. Distinct colors in the attention weights visualizations
represent different attention heads.




resulting hidden state ht , which encapsulates the integrated         adopt two reward configurations: a tight reward with a small
environmental information to estimate the robot’s current             σ to encourage precise goal-reaching behavior, and a loose
state st , is subsequently passed through a multi-layer               reward with a larger σ to promote exploration and stabilize
perceptron (MLP) head to compute the robot’s action at .              training through intermediate guidance.
                                                                         The regularization term rtreg encourages smooth behaviors
4.6      Learning Navigation with Sparse Rewards                      by penalizing rapid action changes and excessive joint
         and Regularizations                                          accelerations. This is implemented using L1 regularization
                                                                      on the difference between the current action at and a
The final attention-based network with the SRU is trained
                                                                      momentum-filtered version of previous actions am      t , as
end-to-end using RL to achieve long-range mapless
                                                                      defined below:
navigation, with the objective of maximizing the cumulative
reward over the episode. The reward function for the                                    am        m
                                                                                         t = λ · at−1 + (1 − λ) · at ,
navigation task is designed as a combination of task-level
rewards rtask , regularization rreg , and penalty rpen terms, as      where λ is the momentum factor. The regularization reward
follows:                                                              is then given by:
                rt = α1 rttask − α2 rtreg − α3 rtpen .
                                                                                 rtreg = β1 · ∥at − am             acc
                                                                                                     t ∥1 + β2 · ∥jt ∥1 ,
Here, α1 , α2 , and α3 are coefficients used to balance the
contributions of the task-level reward, regularization, and           where β1 and β2 are regularization coefficients, and jtacc
penalty terms, respectively. The task-level reward rttask is the      represents joint-level accelerations from the simulation
reward signal that encourages the agent to reach the goal.            environment. The penalty term rtpen discourages unsafe
To promote exploration in complex environments, we adopt              behaviors such as collisions or excessive tilt:
time-based rewards, similar to Rudin et al. (2022); Zhang
et al. (2024); He et al. (2024), that provide feedback at the               rtpen = η1 · 1(collision) + η2 · max(0, |θt | − θsafe )
end of the episode. This approach provides a sparse reward
signal, encouraging the agent to reach the goal without               where η1 and η2 are penalty coefficients, θt is the robot’s
being distracted by intermediate rewards. However, with a             current tilt angle, and θsafe defines the safe tilt threshold.
long episode length Tmax , e.g., 60 seconds, and a rewarding          The reward formulation described above is consistently
period Tr of only 2 seconds, the network may learn to delay           applied throughout the entire RL training process, which
progress until the final step. To mitigate this, we introduce         is conducted end-to-end using an Asymmetric Actor-
a random check during the episode with a small probability            Critic (Pinto et al. 2017) setup and trained with PPO, without
δcheck . This check incentivizes the agent to attempt reaching        employing any additional environment or reward curricula.
the goal earlier, without compromising the overall sparsity           Further training details are provided in Appendix C.
of the reward signal. The final reward formulation is adapted
                                                                      Training Regularization To mitigate overfitting and enhance
from He et al. (2024) and is given as follows:
                                                                      robustness, we incorporate two additional regularization
                                                                      strategies during training. These strategies are crucial for
                    1(t > Tmax − Tr ∨ random < δcheck )               training a robust spatial-temporal representation with SRUs,
         rttask =
                                1 + ∥ pσt ∥2                          as explained below and demonstrated in the experimental
                                                                      results. The regularization techniques are as follows:
where 1(·) is the binary indicator function, Tr is the
rewarding period, ∨ represents the logical OR operation, pt                • Deep Mutual Learning (DML): As described in Xie
is the relative goal position at time t with respect to the                  et al. (2025), DML involves training two policies
current robot pose, and σ is a scaling factor controlling the                simultaneously, enabling them to mutually distill
reward’s spatial sensitivity. Similar to He et al. (2024), we                knowledge from each other. This approach enhances


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                               9


       generalization and mitigates the risk of convergence       success rates (SR). Additionally, we compare the SRU
       to suboptimal solutions. The mutual distillation is        policy, integrated with our proposed network structure and
       achieved by incorporating a Kullback–Leibler (KL)          trained using recurrent RL, against two current state-of-the-
       divergence loss between the two policies, both of          art (SOTA) baselines (Huang et al. 2023; Lee et al. 2024)
       which are trained using standard proximal policy           for robot navigation with RL. Our evaluation highlights the
       optimization (PPO) (Schulman et al. 2017).                 advantages of the implicit recurrent memory provided by
     • Temporally Consistent Dropout (TC-Dropout): Adapt-         SRU in solving long-range mapless navigation tasks across
       ing from Hausknecht and Wagener (2022), we apply a         diverse environments.
       consistent dropout mask across time steps during both         Furthermore, we ablate the role of our proposed
       rollout and training, ensuring stable memory learning      spatial attention layers in compressing features from
       within the recurrent structure.                            encoded observations to improve memorization and overall
                                                                  navigation performance. We compare our approach against
   As shown in Figure 1, SRUs exhibit a slower convergence
                                                                  the convolution and average pooling method used in
rate for spatial memorization compared to learning temporal
                                                                  Wijmans et al. (2019), as well as the attention mechanism
dependencies, highlighting the inherent complexity and
                                                                  introduced in Huang et al. (2023). We also investigate the
slower pace of learning spatial transformations and forming
                                                                  impact of regularization techniques on training the SRU unit
spatial memory. This discrepancy can lead the network to
                                                                  end-to-end in RL, evaluating their effectiveness in preventing
favor easier-to-learn solutions early in training, relying on
                                                                  early convergence to suboptimal solutions and enhancing
temporal features while neglecting the formation of good
                                                                  navigation performance. Finally, we explain and validate the
spatial memorization, resulting in suboptimal performance.
                                                                  pretrained image encoder’s ability to bridge the sim-to-real
To address this, it is crucial to incorporate regularization
                                                                  gap by demonstrating zero-shot transfer across diverse and
techniques that mitigate early overfitting and promote the
                                                                  complex real-world environments.
exploration and development of more challenging spatial-
temporal features during policy optimization. To tackle
this challenge, we employ deep mutual learning (DML)              5.1    Experimental Setup
strategies tailored for reinforcement learning (RL) (Xie et al.   We conduct our experiments in simulated 3D environments
2025). DML involves training multiple policies in parallel,       using NVIDIA IsaacLab (Mittal et al. 2023), which
allowing them to distill knowledge from one another.              provides a realistic physics engine and fast, parallelizable
This mutual distillation process enhances the network’s           simulation capabilities. The environments are designed to
generalization capabilities and fosters the learning of robust    challenge the robot’s navigation capabilities and include
and essential features. By regularizing each other, the           maze-like structures, randomly generated pillars, stairs, and
models are less likely to converge prematurely to suboptimal      environments with negative obstacles, such as holes and pits,
solutions that rely solely on easy-to-learn features, such        as shown in Figure 6. The robot is equipped with front-facing
as temporal dependencies. Instead, DML encourages the             depth sensors as the only exteroceptive input, capturing the
formation of spatial-temporal representations, leading to         surrounding environment from an egocentric perspective.
improved overall performance. This approach is critical           Additionally, a state estimation and localization module
for leveraging the full potential of the SRU network, as          provides the robot’s proprioceptive state oprop t , including
demonstrated in the experimental results.                         linear and angular velocities (vt and ωt ), projected gravity
   Secondly, compared to standard dropout layers, consistent      (nt ), and the relative goal position (pt ) with respect to the
dropout addresses a critical issue in on-policy reinforcement     robot’s frame at time step t. Given the limited field of view
learning, where standard dropout introduces inconsistent          (FoV) of the depth camera (Horizontal FoV: 105◦ , Vertical
masks between the rollout and training stages (Hausknecht         FoV: 78◦ ) and a maximum range of 10 meters, the robot must
and Wagener 2022). Building on this, we extend consistent         rely on its spatial-temporal mapping capabilities to navigate
dropout with temporal consistency for training the recurrent      through the terrain and reach the designated goal region
structure. Specifically, during the data rollout stage, we        effectively. The robot’s motion is controlled by a set of linear
maintain the same dropout mask across all time steps,             and angular velocities, referred to as the action at , which
ensuring temporal consistency. During the training stage,         is the output of the policy network. The navigation policy
the same dropout mask is applied to the policy network.           operates at a frequency of 5 Hz. The robot is equipped with
This approach promotes stable memory learning through             a learning-based locomotion controller (Lee et al. 2024),
recurrent connections and enhances the robustness of the          operating at 50hz. This controller takes the action output
learned policy.                                                   at from the high-level navigation policy and executes it to
                                                                  control the robot. The policies are trained end-to-end using
5     Experiments                                                 reinforcement learning, without employing any distillation or
                                                                  teacher-student setups.
To evaluate the effectiveness of the proposed Spatially-
Enhanced Recurrent Unit (SRU) and the attention-based
network architecture in enhancing long-horizon robot              5.2    Comparsion with Recurrent Units
navigation, we conduct experiments in both simulated and          We evaluate the performance of the proposed Spatially-
real-world environments. We compare the SRU against               Enhanced Recurrent Units (SRUs) compared to standard
standard LSTM and GRU units in long-range mapless                 LSTM and GRU units. Given the superior spatial
navigation tasks, focusing on their performance in end-to-        memorization capability of SRUs, as demonstrated in
end reinforcement learning (RL) training and navigation           Figure 1, we hypothesize that integrating SRUs will improve


Prepared using sagej.cls
10                                                                                                                                    ()




                                                                                                                                A



                                                                                                                                B



                                                                                                                                C



                                                                                                                                D
Figure 6. Simulated environments used for training and testing RL-based navigation tasks: (A) Maze, (B) Random Pillars, (C)
Stairs, and (D) Pits. These environments are parameterizable and can be randomly generated during both training and testing
using the NVIDIA IsaacLab (Mittal et al. 2023) simulation framework.



                                                                                                           START
                                                                       GOAL          B
                                                             START
 GOAL
         C           B

                             START                                                                         A

                                 A

                                                                                          A

                                                                                              START
                                            GOAL

                                                                                                               GOAL
                                     MAZE                    PILLAR                           STAIR                             PIT

                                                   (a) Navigation Policy with LSTM Unit

                                                           START
  D                                                                                                        START
                                                                              GOAL
         C               B
 GOAL
                             START


                             A




                                            GOAL                                              START

                                                                                                               GOAL
                                     MAZE                     PILLAR                           STAIR                            PIT

                                                   (b) Navigation Policy with SRU Unit


Figure 7. Comparison of navigation trajectories using (a) Navigation Policy with LSTM Unit and (b) Navigation Policy with
SRU-Ours. The traversed trajectories are shown in yellow. In maze environments, the LSTM policy becomes trapped in a dead-end
corridor, repeatedly looping between points B and C, while the SRU policy successfully navigates through the corridor, traverses
region D, and reaches the goal. In stair-like environments, the LSTM policy exhibits frequent back-and-forth movements in areas A
and B, indicating unreliable spatial-temporal mapping. In pit environments, the LSTM policy fails to avoid previously encountered
pits during turns at area A, whereas the SRU policy effectively recalls their locations and avoids them, even during backward motion.




the performance of navigation policies in addressing long-             are equipped with the same components (attention, training
range mapless navigation tasks. To test this hypothesis, we            regularization, and a pretrained encoder); only the recurrent
train, under same conditions, policy networks integrated               network structure differs. We then evaluate their navigation
with different recurrent units end-to-end using RL in the              performance.
simulated 3D environments shown in Figure 6. All policies


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                   11


                                                                     the performance in success rate compared to standard LSTM
                                                                     and GRU units.
                                                                        Figure 7 presents example traversed trajectories compari-
                                                                     son between the SRU and standard LSTM policies. In maze
                                                                     environments, the LSTM policy gets trapped in a dead-
                                                                     end corridor, looping between points B and C, while the
                                                                     SRU policy successfully passes through the corridor, demon-
                                                                     strating better spatial memorization capability. In stair-like
                                                                     environments, although the LSTM eventually reaches the
                                                                     destination, it exhibits frequent back-and-forth movements
                                                                     (areas A and B), indicating less reliable spatial-temporal
                                                                     memorization and estimation of the current state compared to
                                                                     the policy with SRU. In pit environments, the LSTM policy
Figure 8. Training curve comparison between policies                 fails to avoid the previously encountered pits that are no
integrated with different recurrent units: The average return from   longer visible in the current depth observation, when turning
three random seeds during training. The architecture with SRU
                                                                     at area A. In contrast, the SRU policy effectively recalls the
units achieves a higher return compared to the baseline LSTM
and GRU units.
                                                                     locations of the pit and other previously observed obstacles,
                                                                     enabling it to avoid them during turns and backward motion.


                  Navigation Success Rate - SR %
                                                                     5.3    Comparsion against RL-based Navigation
                                                                            Baselines
  Model                Maze       Pillar   Stair   Pit    Overall
                                                                     Next, we compare our proposed network structure, trained
  GRU                      68.1   73.6     35.7    66.7    61.0      using recurrent reinforcement learning with SRU, against
  LSTM                     70.3   78.2     33.1    72.7    63.5      two state-of-the-art RL baseline methods: the Goal-guided
                                                                     Transformer-based RL approach (GTRL) (Huang et al.
  SRU-GRU                  73.1   78.8     74.1    74.8    75.2
                                                                     2023) and the RL approach with Explicit Mapping and
  SRU-LSTM                 75.9   76.7     79.3    74.1    76.5
                                                                     Historical Path (EMHP) (Lee et al. 2024). GTRL employs a
  SRU-Ours                 76.0   81.0     82.8    75.6    78.9
                                                                     goal-guided Transformer (GoT) architecture to extract task-
Table 1. Navigation success rate (SR) for policies integrated        relevant visual features from stacked historical observations,
with different recurrent units across four environment types:        enabling mapless navigation using only egocentric input.
Maze, Random Pillars, Stairs, and Pits. The table compares           EMHP employs an external mapping pipeline to integrate
standard LSTM and GRU units with our proposed spatially              historical observations for local mapping (Miki et al. 2022b)
enhanced counterparts: SRU-GRU, SRU-LSTM, and SRU-Ours.              and uses an explicit historical traversed path to address
                                                                     POMDP challenges in long-range mapless navigation. While
                                                                     explicit mapping (EMHP) can theoretically achieve high
   As shown in Figure 8, the policy with the SRU memory              accuracy in spatial-temporal registration, it has two major
unit is able to outperform those with standard LSTM and              drawbacks: (i) it introduces significant delays that hinder
GRU units in terms of average return episode rewards                 real-time performance, especially on high-speed, agile
during training, with results averaged across multiple random        platforms (Lee et al. 2024), and (ii) it relies on heuristic rules
seeds. (Note: GRU training can exhibit instability, so only          (e.g., fixed context window lengths) to select information,
its successful runs are included in the analysis.), Table 1          limiting its ability to capture complex spatial-temporal
provides a summary of the navigation performance for                 dependencies and abstract information beyond the selected
policies using different architectures. The best-performing          context window.
model from each unit (determined by the highest average                 Figure 9(a) presents a comparison between the EMHP
return rewards) is selected for comparison. The data is              baseline and our SRU-based approach. The EMHP policy
averaged over 4800 episodes across 120 randomly generated            collects historical paths for approximately 20 meters, which
environments, which are different from the training set.             is insufficient to navigate the long corridor spanning around
The results are presented in terms of success rate (SR) for          30 meters. In contrast, recurrent neural networks offer an
each environment. The SRU units consistently outperform              unlimited context window and can learn intricate spatial-
the standard LSTM and GRU units, achieving an average                temporal dependencies optimized for the given task. This
21.8% improvement in SR across all environments with                 allows the SRU-based policy to adapt to long-horizon
the SRU modification alone. Furthermore, incorporating the           navigation challenges more effectively. Moreover, our end-
refined gating mechanism in the SRU-Ours model further               to-end architecture processes raw depth sensor inputs,
boosts the results, achieving an overall 23.5% increase in           reducing latency and better supporting the agile and fast
SR, demonstrating the effectiveness of these enhancements            motion of legged-wheel platforms during deployment. For
in improving navigation performance. Notably, in stair-              the GTRL baseline, temporal history is provided by stacking
like environments, where the 3D structure and significant            several past observation frames, which are then fused using
occlusions pose challenges for navigation without precise            the transformer-based architecture as described in (Huang
spatial memorization and registration capabilities, the              et al. 2023). Following the original approach in Huang et al.
navigation policy with SRU units demonstrate over double             (2023), we use the 4-frame history in our experiments.


Prepared using sagej.cls
12                                                                                                                               ()


However, the choice of the number of stacked frames                                     Method                     SR (%)
remains heuristic: a short history may miss important
context, while a longer history increases computational cost                 GTRL (w. historical obs.)                38.2
quadratically. For a fair comparison, we retrain the GTRL                 EMHP (w. explicit mapping / path)           60.4
baseline, as described in Huang et al. (2023), within our
                                                                              GTRL* (w. SRU memory)                   66.3
environment. We replace the RGB input with depth images
                                                                               Ours (w. SRU memory)                   78.3
and utilize the same on-policy optimization method (PPO)
for end-to-end RL training. To ensure consistency with the         Table 2. Overall navigation success rate (SR) comparison
platform utilized in Lee et al. (2024), this comparison is         against baselines. Policies with SRU implicit recurrent memory
conducted using the simulated wheeled ANYmal (Hutter               outperform: (i) GTRL (stacked historical observations) and (ii)
et al. 2016) robot model, which differs from the robot model       EMHP (explicit mapping and historical path). GTRL* denotes
                                                                   our modified GTRL variant where stacked observations are
used in the other comparisons in this paper. All policies
                                                                   replaced by SRU implicit memory, yielding a substantial gain
are trained under identical conditions and evaluated on an         over the original GTRL baseline.
independent test environment set to ensure a fair comparison.
Note that our policy and the GTRL baseline rely solely on
a front-facing camera with a limited field of view, whereas
the EMHP approach incorporates a local height scan with a                      Attention Configuration        SR (%)
similar range for environmental detection but benefits from a                        w/o. Attention            50.5
complete 360-degree field of view for mapping.                                      GoT (GTRL*)                68.4
   The experimental results (see Table 2) indicate that our                     Spatial Attention (Ours)       78.9
architecture, leveraging an implicit memory representation
                                                                   Table 3. Navigation success rate (SR) for policies integrated
within the recurrent module, outperforms both baselines.
                                                                   with different attention configurations. The policy with the
Compared to EMHP, it achieves a 29.6% relative improve-            proposed spatial attention (Ours) achieves the highest SR,
ment in SR. Against GTRL, it demonstrates a remarkable             outperforming (i) the baseline without attention Wijmans et al.
105.0% relative improvement. These results underscore the          (2019) and (ii) the Goal-guided Transformer (GoT) Huang et al.
limitations of explicit mapping or stacked-frame histories for     (2023) integrated with SRU memory (GTRL* approach in
long-horizon navigation under limited context. Figure 9(a)         Sec. 5.3), highlighting the importance of an attention
illustrates a representative comparison: in a long-horizon         mechanism for training mapless navigation end-to-end and the
                                                                   effectiveness of the proposed spatial attention structure.
maze environment, the EMHP approach, despite achieving a
relatively higher SR among the two baselines, is constrained
by the limited horizon of its explicit memory, fails to navigate
through the maze and eventually loops in a long corridor. In
                                                                   is extended to 120 seconds, the EMHP’s SR still declines
contrast, our policy successfully traverses a dead-end corri-
                                                                   to below 60% at the same 40-meter distance, constrained
dor and reaches the goal, demonstrating the effectiveness of
                                                                   by its fixed context window. Conversely, our SRU-based
the SRU unit in learning implicit spatial-temporal mapping
                                                                   approach sustains an SR of over 70% for distances up to
for long-horizon navigation tasks. To further validate the
                                                                   120 meters, demonstrating the SRU’s superior ability to
effectiveness of SRU for implicit spatial-temporal memo-
                                                                   implicitly learn spatial-temporal mappings and generalize
rization in mapless navigation, we replaced GTRL’s stacked
                                                                   to distances beyond the training range. The baseline’s
historical observations with our SRU-based recurrent mem-
                                                                   reliance on a fixed explicit memory window limits its
ory while keeping all other components unchanged. This
                                                                   capacity to capture long-range dependencies, hindering its
modified variant, denoted GTRL*, achieves a 73.6% relative
                                                                   generalization in extended long-distance navigation tasks.
improvement over the original GTRL baseline, increasing
                                                                      Furthermore, we observed that the EMHP policy struggles
the SR from 38.2% to 66.3% (Table 2). This substantial
                                                                   to effectively learn to climb staircases unless dense reward
gain highlights the advantage of SRU’s implicit recurrent
                                                                   guidance is provided. We believe this limitation arises from
memory over heuristic stacking of historical observations
                                                                   the inherent difficulty explicit memory mechanisms face
in capturing spatial-temporal dependencies for improved
                                                                   in capturing intricate spatial-temporal features, which are
navigation performance. Notably, compared to GTRL*, our
                                                                   essential for the robot to develop the maneuvers required
complete SRU-based approach (Ours) achieves an additional
                                                                   to overcome 3D obstacles effectively. Lastly, the end-to-
18.1% relative improvement, attributable to our proposed
                                                                   end recurrent setup offers a simpler and more maintainable
spatial attention layers. The impact of these attention layers
                                                                   solution compared to baseline methods. In contrast, baselines
is further discussed later.
                                                                   rely on an external mapping pipeline and the storage of
   Quantitatively, while the EMHP approach achieves                additional historical paths or observations for each robot,
comparable navigation performance, we also analyze the             which can introduce complexity and overhead during both
success rate (SR) as a function of travel distance to evaluate     training and real-world deployment.
its long-range memorization and generalization capabilities.
As shown in Figure 10, with a maximum episodic time of 60
seconds (consistent with training) and the robot’s maximum         5.4    Importance of Spatial Attention Layers
speed set to 1.5 m/s, the EMHP approach’s SR drops                 We now examine the role of the proposed spatial attention
significantly when the travel distance exceeds 40 meters. In       layers in the network architecture and evaluate their impact
contrast, our SRU-based approach maintains an SR of over           on navigation performance. These layers are designed to
80% up to 50 meters. When the maximum episode time                 compress and emphasize relevant features from encoded

Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                 13


                                                                     observations, addressing a key challenge faced by recurrent
                                                                     structures: the difficulty of retaining long-term information
                                              B
                                                                     due to the exponential decay of memory over time. By
                           C                                         selectively focusing on the most salient features, the attention
          GOAL                                                       mechanism emphasizes the most relevant spatial cues for
                                                          START
                                                                     navigation based on the robot’s state and reduces the
                                                                     information density passed into the recurrent memory at
                                                                     each step. We hypothesize that this mechanism can improve
                                                   A                 the network’s memorization and navigation capabilities,
                                                                     enabling it to handle complex, long-range tasks more
                                                                     effectively.
                                                                        To test this, we conduct an ablation study by: (i)
                                                          MAZE
                                                                     removing the attention layers from our network architecture
       (a) Policy with Explicit Mapping and Historical Path (EMHP)   and replacing them with convolution followed by average
                                                                     pooling for feature compression, as implemented in Wijmans
               D
                                                                     et al. (2019), and (ii) comparing the performance of our
                                                                     proposed spatial attention layers against the Goal-guided
                           C                   B                     Transformer (GoT) architecture proposed in Huang et al.
                                                                     (2023). The GoT architecture utilizes a modified Vision
            GOAL                                          START      Transformer (ViT) that integrates the goal state as an
                                                                     additional token. It performs self-attention across both
                                                                     visual feature tokens and the goal token to extract goal-
                                                   A                 relevant features. In contrast, our approach first applies
                                                                     self-attention exclusively to visual tokens to enhance
                                                                     spatial features. Subsequently, the goal and proprioceptive
                                                                     state are used as queries in the cross-attention layer
                                                          MAZE       to compress and extract the most relevant features. For
                   (b) Policy with SRU Recurrent Memory
                                                                     a fair comparison in the ablation experiments, we use
                                                                     identical training settings for all approaches, integrating
Figure 9. Comparison of proposed mapless method with SRU
                                                                     the SRU memories and the pretrained encoder while
recurrent memory against the EMHP baseline approach in a             varying only the attention layers used to process visual
maze environment. The robot’s traversed trajectory is shown in       features during RL. The GoT integrated with SRU is
yellow, with traversal order marked as A, B, C, and D. (a) The       the the GTRL* approach, as described in Sec. 5.3.
EMHP approach starts looping in the long corridor between            Figure 12 shows the average return rewards during
points B and C, failing to navigate through the dead-end             training. The network without the attention layers exhibits
corridors. (b) Our approach, with SRU recurrent memory,              significantly lower performance compared to the two policies
successfully navigates from start to goal, rerouting through the
dead-end corridors and reaching the goal through area D.
                                                                     utilizing attention mechanisms. Additionally, our proposed
                                                                     spatial attention layers outperform the GoT attention
                                                                     mechanism. Table 3 shows the SR performance of the
                                                                     three configurations: (i) without attention, (ii) with GoT
                                                                     attention, and (iii) with our proposed spatial attention (Ours).
                                                                     Our method achieves a 56.2% relative SR improvement
                                                                     over the no-attention baseline, highlighting the importance
                                                                     of selectively compressing and extracting spatial features
                                                                     for long-range mapless navigation when utilizing implicit
                                                                     recurrent memory. Furthermore, it achieves a 15.4% relative
                                                                     improvement (18.1% when trained with the ANYmal robot
                                                                     model, as shown in Table 2) over the policy utilizing GoT
                                                                     attention. This demonstrates that the proposed two-stage
                                                                     spatial attention mechanism more effectively extracts task-
                                                                     relevant cues, enhancing recurrent memorization and policy
                                                                     optimization.
Figure 10. Success rate sorted by travel distance: comparison           Notably, the attention effect emerges naturally during
between the EMHP baseline approach, which uses explicit              the end-to-end RL training without requiring additional
mapping and a fixed-length historical path, and our approach,        supervision or auxiliary losses. Figure 11 illustrates the
which employs the implicit recurrent memory of SRU. Our              attention weights generated by the cross-attention layer over
method maintains a high success rate over longer distances           raw visual inputs in three distinct real-world deployment
and extends effectively with longer episodic times. In contrast,
the baseline’s success rate drops significantly for longer travel
                                                                     scenarios: an indoor office, an outdoor terrace, and a forest
distances, even when the maximum episodic time is doubled,           environment. The attention weights, with four attention
due to its fixed context window limitation.                          heads (depicted in different colors), dynamically emphasize
                                                                     the most relevant spatial cues, such as obstacles and


Prepared using sagej.cls
14                                                                                                                                  ()




                (a) Office Environment                  (b) Terrace Environment                     (c) Forest Environment

Figure 11. Visualization of attention weights for the cross-attention layer in three distinct real-world deployment scenarios over raw
depth inputs: (a) Office environment, (b) Outdoor terrace environment, and (c) Forest environment. The attention weights
dynamically highlight relevant spatial cues for navigation based on the robot’s state. The RGB images in the top corners are
included for visualization purposes only.




                                                                     overly rely on easier-to-learn temporal features to solve
                                                                     navigation tasks, thereby failing to establish robust spatial-
                                                                     temporal memorization. To test this hypothesis, we conduct
                                                                     an ablation study by removing the regularization techniques,
                                                                     specifically deep mutual learning (DML), from the standard
                                                                     PPO training setup and comparing the performance against
                                                                     the setup with DML regularization.
                                                                        Figure 13 illustrates that the network without DML
                                                                     exhibits lower average return rewards during training.
                                                                     Notably, the performance difference between standard
                                                                     LSTM and SRU modifications becomes more pronounced
                                                                     when regularization techniques are applied. As shown in
                                                                     Table 4, the SR performance improves from 61.8% to
Figure 12. Average training return rewards for attention             65.7% (a 6.3% increase) without DML and from 63.5%
ablations (all using SRU recurrent memory): (1) without              to 78.9% (a significant 24.3% increase) with DML. This
attention (w/o.) Wijmans et al. (2019); (2) Goal-guided              finding underscores that, in certain RL tasks, the network’s
Transformer (GoT) attention Huang et al. (2023); and (3) the
                                                                     architecture alone may not be the sole limiting factor.
proposed two-stage spatial attention (Ours). The proposed
spatial attention achieves the highest returns, indicating more      Instead, the optimization process plays a critical role in
effective extraction of task-relevant spatial cues for improved      fully leveraging the network’s potential, highlighting the
recurrent memorization.                                              importance of effective training strategies.
                                                                        Additionally, we observe that incorporating the consistent
                                                                     dropout layer with temporal consistency into the recurrent
                                                                     training can also positively impact navigation performance,
navigable free space, based on the robot’s state at the time the     as shown in Table 5. This enhancement improves the SR
depth input was recorded. This highlights the effectiveness          when tested in new, randomly generated environments.
of training the spatial attention mechanism end-to-end and           These findings align with the discussion in Hausknecht
its ability to generalize across diverse and challenging             and Wagener (2022), which highlights the benefits of
environments.                                                        using dropout in RL training to enhance the network’s
                                                                     generalization and robustness.
5.5      Training with Regularizations
We evaluate the role of regularization techniques in the end-        5.6     Large-Scale Pretraining for Sim-to-Real
to-end training of the recurrent network using reinforcement                 Transfer
learning. Firstly, as shown in Figure 1 and discussed in             In this section, we evaluate the pretrained image encoder,
Sec. 4.6, while the SRU unit effectively enhances the                trained on a large-scale synthetic dataset, for its ability
network’s ability to learn implicit spatial memorization             to bridge the sim-to-real gap in real-world perception.
from sequential observations, the learning curve indicates           Additionally, we assess the effectiveness of the proposed
that spatial memory learning can converge significantly              depth noise model in reducing discrepancies between
slower than temporal memorization. This discrepancy,                 synthetic and real-world data. To this end, we conduct
combined with the inherent properties of standard policy             zero-shot transfer experiments on legged-wheel platforms
optimization algorithms like PPO—which restrict deviations           across diverse real-world environments to demonstrate the
from previous optimization steps—and the complex structure           generalization of our approach.
of attention networks with RNNs prone to overfitting,
suggests that without proper regularization, the network may         Pretrain and Depth Noise. Here, we analyze the latent
converge to suboptimal strategies. Such strategies might             space distribution of encoders trained under two distinct


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                              15


                                                                   distribution range that encompasses the features extracted
                                                                   from real-world data when derived from the encoder
                                                                   pretrained on large-scale synthetic data (Figure 15(a)). This
                                                                   indicates that the encoder pretrained on large-scale synthetic
                                                                   data effectively captures a wide range of features, enabling
                                                                   it to generalize well to real-world scenarios. In contrast, the
                                                                   encoder trained solely on RL images (Figure 15(b)) exhibits
                                                                   a narrower latent space distribution, failing to cover many
                                                                   real-world features. This suggests that an encoder trained
                                                                   exclusively on simulated depth images collected during RL
                                                                   navigation training may struggle to generalize effectively to
                                                                   real-world data when deployed.
                                                                       Additionally, Figure 14 provides a qualitative comparison
Figure 13. Training curve comparison between policies trained      of depth reconstruction using features extracted from the
using PPO with deep mutual learning (DML) regularization and       same two pretrained encoders. The comparison is based on a
PPO: The network with DML regularization techniques achieves
                                                                   real-world stereo depth input captured during deployment.
higher returns compared to the network trained with vanilla
PPO.                                                               The encoder pretrained on large-scale data demonstrates
                                                                   effective reconstruction of the depth image, with only minor
                                                                   blurring effects (Figure 14(b)). In contrast, the encoder
                                                                   trained solely on RL images struggles to reconstruct the input
                   RL Training            SR %                     depth image effectively, resulting in outputs with significant
                   LSTM w/o. DML           61.8                    artifacts and noise (Figure 14(c)).
                   LSTM w. DML             63.5                        To quantitatively assess the distributional disparity of
                                                                   features from encoders trained on different sources, we
                   SRU-Ours w/o. DML       65.7                    adapt the method from Lee et al. (2018) to measure the
                   SRU-Ours w. DML         78.9                    Mahalanobis distance (MD) for the latent distributions
                                                                   derived from each encoder. In addition to the two pretraining
Table 4. Comparison of the overall navigation success rate
(SR) with and without DML regularization for policies using
                                                                   sources mentioned earlier, we also analyze the latent
LSTM and SRU units. DML significantly enhances SR for SRU          distribution of the encoder pretrained on large-scale synthetic
(over 20%) and provides a marginal improvement for LSTM            data without noise augmentation. This allows us to evaluate
(2.8%), showcasing DML’s effectiveness in unlocking SRU’s          the effectiveness of the proposed depth noise model in
potential for long-range mapless navigation.                       further reducing the sim-to-real gap between synthetic depth
                                                                   images and real-world stereo depth. The MDs are computed
                                                                   between the latent features of real-world images and the
                  RL Training            SR (%)                    latent feature distributions of RL images extracted from
                                                                   each encoder. As shown in Figure 16, pretraining on large-
                  SRU-Ours w/o. TC-D       77.2                    scale synthetic data effectively reduces the MD, lowering the
                  SRU-Ours w. TC-D         78.9                    median from 1.15 (RL images) to 0.82 (large-scale synthetic
                                                                   data without noise). This demonstrates the pretrained
Table 5. Evaluation of the overall navigation success rate (SR)
with and without temporally consistent dropout (TC-D): The         encoder’s effectiveness in covering the distribution of real-
network with TC-D is able to maintain a similar (or even higher)   world perception inputs. Furthermore, incorporating the
SR compared to the network without TC-D, while improving           proposed depth noise model further reduces the MD to
robustness and generalization.                                     0.69, underscoring its role in narrowing the differences
                                                                   between synthetic and real-world depth data. These results
                                                                   highlight that the encoder, pretrained on large-scale data
                                                                   and augmented with the proposed depth noise model, can
conditions: (i) an encoder trained exclusively on simulated        effectively minimize the sim-to-real gap, enabling improved
depth images generated during RL navigation training               generalization to real-world environments.
(RL images), (ii) an encoder pretrained on large-scale
synthetic data from Wang et al. (2020), augmented with             Real-world Tests on Legged-wheel Robot. To evaluate
the proposed parallelizable depth noise model (Figure 4).          the pretrained image encoder’s with the proposed attention-
To evaluate these encoders, we compare the latent features         based recurrent network’s ability to generalize across in real-
extracted from their outputs using two data sources: (i) RL        world environments, we conduct several zero-shot transfer
images, and (ii) real-world stereo depth images captured by        experiments, on a Unitree B2W robot with a learning-
the ZEDX camera during deployment (real-world images).             based locomotion policy from RIVR. The robot is mounted
This analysis highlights their differences in latent space         with a ZEDX, front-facing stereo depth sensor, and NVIDIA
distributions depending on the pretraining data source used        Jetson AGX Orin for onboard compute for the policy. The
for the encoder.                                                   pretrained encoder and network are directly deployed on
   Figure 15 illustrates a 2D principal components analysis        the robot without any fine-tuning with real-world data.
(PCA) (Dunteman 1989) projection of the latent features.           For all the test, the robot receives no prior information
The latent space distribution of RL-images shows a larger          about the environment, and receives only the stereo depth


Prepared using sagej.cls
16                                                                                                                                                  ()




         (a) Real-world Stereo Depth Image              (b) Reconstruction with Large-scale Pretrain   (c) Reconstruction with RL-images Pretrain


Figure 14. Comparison of depth image reconstruction using features from encoders pretrained on different data sources. (a)
Original input stereo depth image from real-world deployment, captured using the ZEDX camera. (b) Reconstructed depth image
using features extracted from the encoder pretrained on large-scale synthetic data with noise augmentation. (c) Reconstructed
depth image using features extracted from the encoder trained exclusively on simulated images collected during RL navigation
training.




                                                                                                       1.15

                                                                                                                         0.82
                                                                                                                                         0.69




       (a) Latent space distribution with large-scale data pretraining
                                                                               Figure 16. Comparison of Mahalanobis distances between the
                                                                               latent features of real-world images and the latent feature
                                                                               distributions of RL images, using encoders pretrained on
                                                                               different sources: (i) RL images, (ii) large-scale synthetic data
                                                                               without noise augmentation, and (iii) large-scale synthetic data
                                                                               with noise augmentation.




                                                                               vt and ωt , projected gravity nt , and relative goal position pt
                                                                               with respect to the robot’s frame. The robot is controlled by
                                                                               a set of linear and angular velocities, referred to as action at ,
                                                                               which is the input to the locomotion policy.
                                                                                  Firstly, we conduct an experiment in an office environ-
                                                                               ment, as shown in Figure 17, to compare the navigation
          (b) Latent space distribution with RL images pretraining             performance of our policy with the SRU memory module
                                                                               against a baseline model using a standard LSTM unit. In
Figure 15. Comparison of latent space distributions: (a) The                   this experiment, the robot is tasked with navigating from
feature distribution from the encoder pretrained on large-scale
                                                                               one side of the office to the other while avoiding obstacles.
synthetic data effectively covers the distribution of real-world
data, indicating better generalization. (b) The feature distribution           To evaluate the long-term spatial-temporal memorization
from the encoder trained solely on simulated data collected                    capabilities of the SRU module, several passageways are
during RL fails to cover the distribution of real-world depth                  temporarily blocked, requiring the robot to backtrack and
images, posing challenges in generalizing to real-world data.                  search for alternative routes to reach the goal. Additionally,
                                                                               dynamic changes are introduced by unblocking certain areas
                                                                               during navigation to further assess the robustness of the
                                                                               SRU-enhanced policy. The policy with SRU demonstrates
images from the front-facing camera as the exteroceptive                       the ability to explore dead ends, navigate around obsta-
input. Additionally, a LiDAR-based state estimation and                        cles, and re-evaluate its path to adapt to dynamic changes
localization module (Chen et al. 2023) provide the robot’s                     in the environment (Figure 17(a)). The robot successfully
proprioceptive state, including linear and angular velocities                  reaches the goal, showcasing the effectiveness of utilizing

Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                   17




                                                                        START
                                                    GOAL                (GOAL)       A
                                           C                                                                              B


                                                    B
                                     A                                                    C
             START
                                                                                                                        GOAL
                                                                                                                       (START)

      A                    B                   C                        A                 B                        C




                       (a) With SRU Memory Module                                             (a) Main Hall




                                                                                                                          START
                                                                            B             GOAL                            (GOAL)
                                                                                         (START)        C




                                                                                                    A


                                                                        A                 B                        C
                 (b) With Standard LSTM Memory Module


Figure 17. Comparison of navigation trajectories (orange) in an
office environment. A, B, and C indicate areas that the robot
traverses in sequence. (a) shows that the robot using the SRU                                  (b) Terrace
memory module successfully navigates through two dead ends
and reaches the goal while adapting to changes in the
environment (the blocker located in area A was initially set and
later removed). (b) illustrates that the baseline model with a
standard LSTM fails to reach the goal and repeatedly loops                                    A
                                                                            START
between the dead-end areas C and B.                                         (GOAL)                             B
                                                                                                                           GOAL
                                                                                                                          (START)
                                                                                                               C
the SRU memory module to learn robust spatial-temporal
memorization from sequential observations. In contrast, the
baseline model with a standard LSTM fails to reach the goal             A                 B                        C
and repeatedly loops between dead-end areas, as shown in
Figure 17(b).
   To further evaluate the generalization and performance
of the proposed network architecture in long-horizon
                                                                                                  (c) Forest
navigation tasks, we conduct experiments in a variety of
real-world environments—including an indoor campus main
                                                                   Figure 18. Evaluation of long-range mapless navigation in
hall, outdoor terrace areas, and forest environments—using         diverse real-world environments: (a) Main Hall of a university,
the same pretrained encoder and navigation policy (see             (b) outdoor terrace, and (c) forest environment with natural
Figure 18). In these experiments, the robot is tasked with         obstacles. In each scenario, the robot is tasked with two
navigating to a designated goal and returning to its starting      separate navigation goals (memory reset between goals),
point.Note that the policy is designed to maintain episodic        resulting in two trajectory segments (orange and blue). Labels
memory only between the start and the goal and is reset            A, B, and C mark key areas traversed by the robot.
when a new goal is given. The results demonstrate that
the policy generalizes effectively to unseen environments,
handling diverse obstacles such as walls, stairs, vegetation,
bushes, and trees, as well as navigating uneven terrains.          Note that the maximum start-goal distance during RL
Additionally, the policy adapts to larger-scale scenarios,         training is 30 meters. The figures show the trajectories of the
including extended goal distances of more than 70 meters           robot successfully navigating through these environments,
and traversing over 100 meters, as shown in Figure 18(c).          with point clouds generated from the state estimation


Prepared using sagej.cls
18                                                                                                                                 ()


module (Chen et al. 2023) provided solely for visualization.     which integrate an implicit spatial transformation operation
Note that, due to the absence of a dedicated mapping module      into standard GRU and LSTM structures. These SRUs
or loop closure mechanism, the trajectories shown may            are incorporated into a novel attention-based architecture,
exhibit some drift and errors.                                   trained end-to-end via reinforcement learning, achieving
                                                                 long-horizon navigation tasks with a single forward-
                                                                 facing depth camera. Our research further highlights
6     Limitations and Future Work                                the importance of regularization strategies in end-to-end
While the proposed SRUs in this paper demonstrate signifi-       reinforcement learning frameworks. Techniques such as
cant improvements in spatial-temporal learning capabilities,     temporally consistent dropout and deep mutual learning are
their recurrent nature remains subject to exponential memory     crucial for fully leveraging SRUs’ potential and preventing
decay, which can limit their ability to retain global context    early overfitting. Experiments demonstrate SRUs’ superior
over extended sequences. As a result, the long-range nav-        navigation performance compared to standard LSTM and
igation capabilities presented in this paper are centered on     GRU models. Moreover, we compare our implicit recurrent
local, mapless navigation using egocentric sensing. In this      memory-based approach with a state-of-the-art baseline
context, ”long-range” refers to planning horizons that extend    that utilizes explicit mapping and historical paths. Our
well beyond the local perception radius (e.g., 10 m), enabling   findings illustrate the superior effectiveness of recurrent
rerouting from local dead ends without reliance on an explicit   memory structures for long-range mapless navigation tasks.
global map. Extending this approach to global-scale navi-        Additionally, through ablation studies, we demonstrate the
gation—spanning kilometers or hours—would likely require         role of specific design choices, particularly the spatial
additional mechanisms or architectural enhancements, such        attention mechanism, in enhancing overall navigation
as the integration or maintenance of a global map.               performance. Lastly, we analyze and address the challenge of
   Furthermore, while SRUs enhance the network’s capacity        sim-to-real transfer for stereo depth perception by integrating
for implicit spatial memorization and improve long-range         large-scale pretraining. This approach enables successful
navigation performance, the precise characteristics of the       zero-shot transfer and robust generalization across diverse
information retained and utilized during end-to-end navi-        real-world environments, including indoor, outdoor, and
gation training remain unclear. This highlights a broader        forest scenarios, underscoring the practical applicability and
challenge in explainable artificial intelligence, where under-   effectiveness of our proposed methodology.
standing the internal representations and decision-making
processes of neural networks continues to be an active area
of research (Mi et al. 2024). Future work could explore inte-    Acknowledgements
grating SRUs with recent advancements in foundation pre-         The authors acknowledge Nikita Rudin, Takahiro Miki,
training, such as DINO (Caron et al. 2021), to combine their     Jonas Frey, Pascal Roth, and Chong Zhang for their valuable
strengths in scene understanding with the efficiency of recur-   feedback and discussions. The authors also extend their
rent structures, further enhancing the policy’s performance      gratitude to Marco Trentini for his assistance in conducting
in complex real-world environments. Investigating auxil-         real-world experiments and testing the LiDAR-inertial state
iary losses or additional regularization techniques to further   estimation module. Additionally, the authors recognize the
leverage the potential of spatial-temporal memorization in       RIVR team for their technical support with the legged-wheel
SRUs could also be beneficial. Additionally, extending the       robot platform utilized in this research.
application of SRUs to other domains, such as robotic manip-
ulation and 3D reconstruction, could unlock new possibilities
and advancements in spatial-temporal learning. In summary,       Declaration of Conflicting Interests
while SRUs are effective, they represent a simple yet practi-
                                                                 The authors declared no potential conflicts of interest with
cal solution—not necessarily unique or optimal—that proves
                                                                 respect to the research, authorship, and/or publication of this
successful in our end-to-end mapless navigation context.
                                                                 article.
More importantly, this work aims to highlight the potential of
implicit spatial memory mechanisms in addressing complex
navigation challenges while identifying opportunities for        References
further exploration and optimization in both methodology
and application domains.                                         Barron JT and Malik J (2013a) Intrinsic scene properties from a
                                                                     single rgb-d image. CVPR .
                                                                 Barron JT and Malik J (2013b) Intrinsic scene properties from a
7     Conclusion                                                     single rgb-d image. In: Proceedings of the IEEE Conference
In this study, we identify and address a limitation of               on Computer Vision and Pattern Recognition. pp. 17–24.
existing recurrent neural network architectures in the context   Bhattacharya A, Rao N, Parikh D, Kunapuli P, Wu Y, Tao Y,
of navigation: while RNNs excel at modeling temporal                 Matni N and Kumar V (2024) Vision transformers for end-to-
sequences, they are not inherently designed for spatial              end vision-based quadrotor obstacle avoidance. arXiv preprint
memorization or transforming observations from varying               arXiv:2405.10391 .
perspectives. This limitation makes them less effective in       Bohg J, Romero J, Herzog A and Schaal S (2014a) Robot arm pose
building the spatial representations required for mapless            estimation through pixel-wise part classification. ICRA .
navigation using egocentric perception. To address this,         Bohg J, Romero J, Herzog A and Schaal S (2014b) Robot arm
we propose Spatially-Enhanced Recurrent Units (SRUs),                pose estimation through pixel-wise part classification. In: 2014


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                       19


     IEEE International Conference on Robotics and Automation           Gu A, Goel K and Ré C (2021) Efficiently modeling long sequences
     (ICRA). IEEE, pp. 3143–3150.                                           with structured state spaces. arXiv preprint arXiv:2111.00396
Bohlin R and Kavraki LE (2000) Path planning using lazy                     .
     prm. In: Proceedings 2000 ICRA. Millennium conference.             Gu A, Gulcehre C, Paine T, Hoffman M and Pascanu R (2020b)
     IEEE international conference on robotics and automation.              Improving the gating mechanism of recurrent neural networks.
     Symposia proceedings (Cat. No. 00CH37065), volume 1.                   In: International conference on machine learning. PMLR, pp.
     IEEE, pp. 521–528.                                                     3800–3809.
Bojarski M, Del Testa D, Dworakowski D, Firner B, Flepp B,              Handa A, Whelan T, McDonald J and Davison AJ (2014a) A
     Goyal P, Jackel LD, Monfort M, Muller U, Zhang J et al.                benchmark for rgb-d visual odometry, 3d reconstruction and
     (2016) End to end learning for self-driving cars. arXiv preprint       slam. ICRA .
     arXiv:1604.07316 .                                                 Handa A, Whelan T, McDonald J and Davison AJ (2014b) A
Caron M, Touvron H, Misra I, Jégou H, Mairal J, Bojanowski P and           benchmark for rgb-d visual odometry, 3d reconstruction and
     Joulin A (2021) Emerging properties in self-supervised vision          slam. In: 2014 IEEE international conference on Robotics and
     transformers. In: Proceedings of the IEEE/CVF international            automation (ICRA). IEEE, pp. 1524–1531.
     conference on computer vision. pp. 9650–9660.                      Hart P, Nilsson N and Raphael B (1968) A formal basis for
Cèsar-Tondreau B, Warnell G, Stump E, Kochersberger K                      the heuristic determination of minimum cost paths. IEEE
     and Waytowich NR (2021) Improving autonomous robotic                   Transactions on Systems Science and Cybernetics 4(2): 100–
     navigation using imitation learning. Frontiers in Robotics and         107.
     AI 8: 627730.                                                      Hausknecht M and Wagener N (2022) Consistent dropout for
Chen K, Nemiroff R and Lopez BT (2023) Direct lidar-                        policy gradient reinforcement learning.        arXiv preprint
     inertial odometry: Lightweight lio with continuous-time                arXiv:2202.11818 .
     motion correction. 2023 IEEE International Conference on           He T, Zhang C, Xiao W, He G, Liu C and Shi G (2024)
     Robotics and Automation (ICRA) : 3983–3989DOI:10.1109/                 Agile But Safe: Learning Collision-Free High-Speed Legged
     ICRA48891.2023.10160508.                                               Locomotion.      In: Proceedings of Robotics: Science and
Cho K, Van Merriënboer B, Gulcehre C, Bahdanau D, Bougares                 Systems. Delft, Netherlands. DOI:10.15607/RSS.2024.XX.
     F, Schwenk H and Bengio Y (2014) Learning phrase                       059.
     representations using rnn encoder-decoder for statistical          Hochreiter S and Schmidhuber J (1997) Long short-term memory.
     machine translation. arXiv preprint arXiv:1406.1078 .                  Neural computation 9(8): 1735–1780.
Choi J, Park K, Kim M and Seok S (2019) Deep reinforcement              Hoeller D, Wellhausen L, Farshidian F and Hutter M (2021)
     learning of navigation in a complex and crowded environment            Learning a state representation and navigation in cluttered and
     with a limited field of view. In: 2019 International Conference        dynamic environments. IEEE Robotics and Automation Letters
     on Robotics and Automation (ICRA). IEEE, pp. 5993–6000.                6(3): 5081–5088.
Cimurs R, Suh IH and Lee JH (2021) Goal-driven autonomous               Huang W, Zhou Y, He X and Lv C (2023) Goal-guided transformer-
     exploration through deep reinforcement learning.           IEEE        enabled reinforcement learning for efficient autonomous
     Robotics and Automation Letters 7(2): 730–737.                         navigation. IEEE Transactions on Intelligent Transportation
Dijkstra EW (1959) A note on two problems in connexion with                 Systems 25(2): 1832–1845.
     graphs. Numerische mathematik 1(1): 269–271.                       Hutter M, Gehring C, Jud D, Lauber A, Bellicoso CD, Tsounis V,
Dobson A and Bekris KE (2014) Sparse roadmap spanners                       Hwangbo J, Bodie K, Fankhauser P, Bloesch M et al. (2016)
     for asymptotically near-optimal motion planning.             The       Anymal-a highly mobile and dynamic quadrupedal robot. In:
     International Journal of Robotics Research 33(1): 18–47.               2016 IEEE/RSJ international conference on intelligent robots
Dozat T (2016) Incorporating nesterov momentum into adam .                  and systems (IROS). IEEE, pp. 38–44.
Duarte FF, Lau N, Pereira A and Reis LP (2023) Lstm, convlstm,          Karaman S and Frazzoli E (2011) Sampling-based algorithms for
     mdn-rnn and gridlstm memory-based deep reinforcement                   optimal motion planning. The international journal of robotics
     learning. In: ICAART (2). pp. 169–179.                                 research 30(7): 846–894.
Dunteman GH (1989) Principal components analysis, volume 69.            Kareer S, Yokoyama N, Batra D, Ha S and Truong J (2023) Vinl:
     Sage.                                                                  Visual navigation and locomotion over obstacles. In: 2023
Francis A, Faust A, Chiang HTL, Hsu J, Kew JC, Fiser M and Lee              IEEE International Conference on Robotics and Automation
     TWE (2020) Long-range indoor navigation with prm-rl. IEEE              (ICRA). IEEE, pp. 2018–2024.
     Transactions on Robotics 36(4): 1115–1134.                         Karnan H, Warnell G, Xiao X and Stone P (2022) Voila:
Fu Z, Kumar A, Agarwal A, Qi H, Malik J and Pathak D (2022)                 Visual-observation-only imitation learning for autonomous
     Coupling vision and proprioception for navigation of legged            navigation. In: 2022 International Conference on Robotics and
     robots. In: Proceedings of the IEEE/CVF Conference on                  Automation (ICRA). IEEE, pp. 2497–2503.
     Computer Vision and Pattern Recognition. pp. 17273–17283.          Kavraki LE, Svestka P, Latombe JC and Overmars MH (1996)
Gu A and Dao T (2023) Mamba: Linear-time sequence modeling                  Probabilistic roadmaps for path planning in high-dimensional
     with selective state spaces. arXiv preprint arXiv:2312.00752 .         configuration spaces. IEEE transactions on Robotics and
Gu A, Dao T, Ermon S, Rudra A and Ré C (2020a) Hippo:                      Automation 12(4): 566–580.
     Recurrent memory with optimal polynomial projections.              Kuffner JJ and LaValle SM (2000) Rrt-connect: An efficient
     Advances in neural information processing systems 33: 1474–            approach to single-query path planning. In: Proceedings 2000
     1487.                                                                  ICRA. Millennium conference. IEEE international conference
                                                                            on robotics and automation. Symposia proceedings (Cat. No.


Prepared using sagej.cls
20                                                                                                                                         ()


     00CH37065), volume 2. IEEE, pp. 995–1001.                               arXiv preprint arXiv:1710.06542 .
LaValle SM, Kuffner JJ, Donald B et al. (2001) Rapidly-exploring         Radosavovic I, Kosaraju RP, Girshick R, He K and Dollár P
     random trees: Progress and prospects.          Algorithmic and          (2020) Designing network design spaces. In: Proceedings
     computational robotics: new directions 5: 293–308.                      of the IEEE/CVF conference on computer vision and pattern
Lee J, Bjelonic M, Reske A, Wellhausen L, Miki T and Hutter M                recognition. pp. 10428–10436.
     (2024) Learning robust autonomous navigation and locomotion         Rudin N, Hoeller D, Bjelonic M and Hutter M (2022) Advanced
     for wheeled-legged robots. Science Robotics 9(89): eadi9641.            skills by learning locomotion and local navigation end-to-end.
Lee K, Lee K, Lee H and Shin J (2018) A simple unified framework             In: 2022 IEEE/RSJ International Conference on Intelligent
     for detecting out-of-distribution samples and adversarial               Robots and Systems (IROS). IEEE, pp. 2497–2503.
     attacks. Advances in neural information processing systems          Ruiz-Serra J, White J, Petrie S, Kameneva T and McCarthy C
     31.                                                                     (2022) Towards self-attention based visual navigation in the
Lin TY, Dollár P, Girshick R, He K, Hariharan B and Belongie                real world. arXiv preprint arXiv:2209.07043 .
     S (2017) Feature pyramid networks for object detection. In:         Savinov N, Dosovitskiy A and Koltun V (2018) Semi-
     Proceedings of the IEEE conference on computer vision and               parametric topological memory for navigation. arXiv preprint
     pattern recognition. pp. 2117–2125.                                     arXiv:1803.00653 .
Loquercio A, Kaufmann E, Ranftl R, Müller M, Koltun V and               Schulman J, Wolski F, Dhariwal P, Radford A and Klimov O
     Scaramuzza D (2021) Learning high-speed flight in the wild.             (2017) Proximal policy optimization algorithms. arXiv preprint
     Science Robotics 6(59): eabg5810.                                       arXiv:1707.06347 .
Ma X, Dai X, Bai Y, Wang Y and Fu Y (2024) Rewrite the stars. In:        Shah D, Sridhar A, Bhorkar A, Hirose N and Levine S (2022) Gnm:
     Proceedings of the IEEE/CVF Conference on Computer Vision               A general navigation model to drive any robot. arXiv preprint
     and Pattern Recognition. pp. 5694–5703.                                 arXiv:2210.03370 .
Matthis JS, Yates JL and Hayhoe MM (2018) Gaze and the control           Shah D, Sridhar A, Dashora N, Stachowicz K, Black K, Hirose
     of foot placement when walking in natural terrain. Current              N and Levine S (2023) ViNT: A foundation model for visual
     Biology 28(8): 1224–1233.                                               navigation. In: 7th Annual Conference on Robot Learning.
Mescheder L, Oechsle M, Niemeyer M, Nowozin S and Geiger                 Shi H, Shi L, Xu M and Hwang KS (2019) End-to-end navigation
     A (2019) Occupancy networks: Learning 3d reconstruction in              strategy with deep reinforcement learning for mobile robots.
     function space. In: Proceedings of the IEEE/CVF conference              IEEE Transactions on Industrial Informatics 16(4): 2393–
     on computer vision and pattern recognition. pp. 4460–4470.              2402.
Mi JX, Jiang X, Luo L and Gao Y (2024) Toward explainable                Siami-Namini S, Tavakoli N and Namin AS (2019) The
     artificial intelligence: A survey and overview on their intrinsic       performance of lstm and bilstm in forecasting time series. In:
     properties. Neurocomputing 563: 126919.                                 2019 IEEE International conference on big data (Big Data).
Miki T, Lee J, Hwangbo J, Wellhausen L, Koltun V and                         IEEE, pp. 3285–3292.
     Hutter M (2022a) Learning robust perceptive locomotion for          Surmann H, Jestel C, Marchel R, Musberg F, Elhadj H and Ardani
     quadrupedal robots in the wild. Science robotics 7(62):                 M (2020) Deep reinforcement learning for real autonomous
     eabk2822.                                                               mobile robot navigation in indoor environments. arXiv preprint
Miki T, Wellhausen L, Grandia R, Jenelten F, Homberger T                     arXiv:2005.13857 .
     and Hutter M (2022b) Elevation mapping for locomotion               Sutskever I, Vinyals O and Le QV (2014) Sequence to sequence
     and navigation using gpu. In: 2022 IEEE/RSJ International               learning with neural networks. Advances in neural information
     Conference on Intelligent Robots and Systems (IROS). IEEE,              processing systems 27.
     pp. 2273–2280.                                                      Truong J, Yarats D, Li T, Meier F, Chernova S, Batra D and Rai
Mittal M, Yu C, Yu Q, Liu J, Rudin N, Hoeller D, Yuan JL, Singh              A (2021) Learning navigation skills for legged robots with
     R, Guo Y, Mazhar H, Mandlekar A, Babich B, State G, Hutter              learned robot embeddings. In: 2021 IEEE/RSJ International
     M and Garg A (2023) Orbit: A unified simulation framework               Conference on Intelligent Robots and Systems (IROS). IEEE,
     for interactive robot learning environments. IEEE Robotics and          pp. 484–491.
     Automation Letters 8(6): 3740–3747. DOI:10.1109/LRA.2023.           Wang W, Zhu D, Wang X, Hu Y, Qiu Y, Wang C, Hu Y, Kapoor A
     3270034.                                                                and Scherer S (2020) Tartanair: A dataset to push the limits of
Mohajerin N and Rohani M (2019) Multi-step prediction of                     visual slam. In: 2020 IEEE/RSJ International Conference on
     occupancy grid maps with recurrent neural networks. In:                 Intelligent Robots and Systems (IROS). IEEE, pp. 4909–4916.
     Proceedings of the IEEE/CVF Conference on Computer Vision           Wang Y, Huang X, Sun X, Yan M, Xing S, Tu Z and Li J
     and Pattern Recognition. pp. 10600–10608.                               (2025) Uniocc: A unified benchmark for occupancy forecasting
Ortiz-Haro J, Hönig W, Hartmann VN and Toussaint M (2024) idb-              and prediction in autonomous driving.           arXiv preprint
     a*: Iterative search and optimization for optimal kinodynamic           arXiv:2503.24381 .
     motion planning. IEEE Transactions on Robotics .                    Webb DJ and Berg Jvd (2012) Kinodynamic rrt*: Optimal motion
Pfeiffer M, Schaeuble M, Nieto J, Siegwart R and Cadena C (2017)             planning for systems with linear differential constraints. arXiv
     From perception to decision: A data-driven approach to end-to-          preprint arXiv:1205.5088 .
     end motion planning for autonomous ground robots. In: IEEE          Weerakoon K, Sathyamoorthy AJ, Patel U and Manocha D (2022)
     International Conference on Robotics and Automation (ICRA).             Terp: Reliable planning in uneven outdoor environments
     IEEE, p. 1527–1533.                                                     using deep reinforcement learning. In: 2022 International
Pinto L, Andrychowicz M, Welinder P, Zaremba W and Abbeel P                  Conference on Robotics and Automation (ICRA). IEEE, pp.
     (2017) Asymmetric actor critic for image-based robot learning.          9447–9453.


Prepared using sagej.cls
F. Yang, P. Frivik, D. Hoeller, C. Wang, C. Cadena, and M. Hutter                                                                      21


Wei Y, Zhao L, Zheng W, Zhu Z, Zhou J and Lu J (2023)                  Appendix
    Surroundocc: Multi-camera 3d occupancy prediction for
    autonomous driving.        In: Proceedings of the IEEE/CVF
                                                                       A    Training Details for Spatial-Temporal
    International Conference on Computer Vision. pp. 21729–                 Memorization Task
    21740.                                                             To evaluate the spatial-temporal memorization capabilities of
Wellhausen L and Hutter M (2023) Artplanner: Robust legged robot       different recurrent neural network architectures, we conduct
    navigation in the field. Field Robotics 3: 413–434.                a case study using an abstract version of the spatial-temporal
Wijmans E, Kadian A, Morcos A, Lee S, Essa I, Parikh D,                memorization task shown in Figure 1 and Figure 2. Below,
    Savva M and Batra D (2019) Dd-ppo: Learning near-perfect           we provide the training details for this task. The task
    pointgoal navigators from 2.5 billion frames. arXiv preprint       simulates a scenario where, at each time step t, the recurrent
    arXiv:1911.00357 .                                                 agent receives the following inputs:
Wijmans E, Savva M, Essa I, Lee S, Morcos AS and Batra D (2023)
    Emergence of maps in the memories of blind navigation agents.          • The coordinates of an observed landmark, lti ,
    AI Matters 9(2): 8–14.                                                   represented in the robot’s current frame.
                                                                           • A binary categorical label, ci , associated with the
Wu K, Wang H, Esfahani MA and Yuan S (2021) Learn to navigate
                                                                             landmark.
    autonomously through deep reinforcement learning. IEEE
                                                                           • The ego-centric motion transformation matrix, Mtt−1 ,
    Transactions on Industrial Electronics 69(5): 5342–5352.
                                                                             representing the transformation from the previous
Xie Z, Cao J, Zhang Q, Zhang J, Wang C and Xu R
                                                                             frame to the current frame.
    (2025) The meta-representation hypothesis. arXiv preprint
    arXiv:2501.02481 .                                                 These inputs are concatenated into a 1D vector, passed
Yang F, Cao C, Zhu H, Oh J and Zhang J (2022a) Far planner: Fast,      through a Multi-Layer Perceptron (MLP) layer, and then fed
    attemptable route planner using dynamic visibility update. In:     into the recurrent unit. After T steps, the output MLP layer
    2022 ieee/rsj international conference on intelligent robots and   is tasked with:
    systems (iros). IEEE, pp. 9–16.
Yang R, Zhang M, Hansen N, Xu H and Wang X (2022b) Learning                • Regressing all observed landmark coordinates {lTi , i =
    vision-guided quadrupedal locomotion end-to-end with cross-              1, 2, . . . , T } with respect to the robot’s frame at the
    modal transformers. In: International Conference on Learning             final time step T (spatial memorization task).
    Representations.                                                       • Predicting all observed binary labels {ci , i =
Zeng KH, Zhang Z, Ehsani K, Hendrix R, Salvador J, Herrasti
                                                                             1, 2, . . . , T } associated with the landmarks, which
    A, Girshick R, Kembhavi A and Weihs L (2024) Poliformer:
                                                                             are independent of the observation frame and depend
    Scaling on-policy rl with transformers results in masterful
                                                                             only on the sequential order of observations (temporal
    navigators. arXiv preprint arXiv:2406.20083 .
                                                                             memorization task).
Zhang C, Jin J, Frey J, Rudin N, Mattamala M, Cadena C and             Figure A.1 illustrates the network structure used for training.
    Hutter M (2024) Resilient legged local navigation: Learning        The spatial task is optimized using the Mean Squared Error
    to traverse with compromised perception end-to-end. In: 2024       (MSE) loss, while the temporal task is optimized using the
    IEEE International Conference on Robotics and Automation           Binary Cross-Entropy (BCE) loss. The network is trained
    (ICRA). IEEE, pp. 34–41.                                           using the Nesterov Momentum Adam optimizer (Dozat
Zhu Y, Mottaghi R, Kolve E, Lim JJ, Gupta A, Fei-Fei L and             2016) with an initial learning rate of 2 × 10−3 , which is
    Farhadi A (2017) Target-driven visual navigation in indoor         reduced to 4 × 10−4 after 800 epochs, continuing until 1000
    scenes using deep reinforcement learning. In: 2017 IEEE            epochs are completed.
    international conference on robotics and automation (ICRA).          To ensure the recurrent network does not overfit
    IEEE, pp. 3357–3364.                                               or memorize specific patterns of observed landmarks
                                                                       and associated ego-motion trajectories, the following
                                                                       randomization is applied:

                                                                           • The ego-motion Mtt−1 for each step is uniformly
                                                                             sampled, with translation in the range [−2, 2] meters
                                                                             and orientation in the range [−π, π] radians.
                                                                           • The observed landmark coordinates {lTi , i =
                                                                             1, 2, . . . , T } are uniformly sampled within the
                                                                             range [−5, 5] meters relative to the observation frame,
                                                                             and the binary categorical labels {ci , i = 1, 2, . . . , T }
                                                                             are uniformly sampled from the set {0, 1}.


                                                                       B    Parallelizable Stereo Depth Perception
                                                                            Noise Implementation
                                                                       The following pseudocode B.1 injects synthetic stereo depth
                                                                       images with edge noise, filling noise, and round noise to
                                                                       simulate realistic sensor artifacts. This implementation is


Prepared using sagej.cls
22                                                                                                                                   ()


                                                                       C    Training Details for Navigation with
                                                                            Reinforcement Learning
                                                                       This section provides the training and parameter details
                                                                       for the end-to-end navigation task using reinforcement
                                                                       learning. We utilize an asymmetric actor-critic setup, training
                                                                       with the NVIDIA IsaacLab simulation framework. The
                                                                       actor processes noisy observations, including depth input
Figure A.1. Network architecture for the spatial and temporal          with noise augmentation, using the spatial attention-based
memorization task. At each step t, the agent receives landmark
coordinates lti , a binary label ci , and ego-centric motion Mtt−1 .
                                                                       recurrent structure. In contrast, the critic has access to
These inputs are concatenated, passed through an MLP layer,            additional 360-degree height scan information alongside the
and processed by a recurrent unit. After T steps, the MLP head         depth input. These inputs are processed separately through
is tasked with recalling, from the final hidden state of the           two attention layers, which are then concatenated before
recurrent unit, all observed landmark positions {lTi } with            being passed to the SRU unit. Unlike the actor, the critic does
respect to the final frame T (spatial task) and sequentially           not use noise-augmented observations. To handle the height
predicting the associated labels {ci } (temporal task).                scan input for the critic, we pretrain a height scan encoder
                                                                       with the same architecture as the depth encoder, using height
                                                                       scan images collected from the RL simulation environments.
used both during pretraining on synthetic depth data and               To improve the network’s generalization for handling large
during online reinforcement learning to better mimic real-             distance values in long-range navigation, we convert the goal
world sensor imperfections.                                            position pt ∈ R3 into a unit directional vector and a log-
                                                                       transformed distance value. This transformation allows the
  Inputs: The function takes depth (RB×H×W ), a batch of               network to generalize better to varying distances.
raw depth image tensors, where B indicates the batch size,                To enhance sim-to-real transfer, we introduce randomiza-
and H and W represent the spatial dimensions of the depth              tion noise to the actor’s observations. The noise parameters
image, specifically its height and width.                              applied during training are summarized in Table C.1. The
  Parameters: The parameters include f (focal length                   critic, in contrast, receives clean observations without any
of the camera), b (baseline between stereo cameras),                   noise or delay, ensuring stable and accurate value estimation
filt size (local window size for filtering), τ min                     during training. These randomization strategies, combined
and τ max (edge noise threshold range), ρ min and
ρ max (pseudo-stereo match probability range), and                            Observation Parameter         Noise Range (U)
invalid disp (value to mark dropped disparities).                             Linear Velocity (vt )             ±0.2 m/s
                                                                              Angular Velocity (ωt )           ±0.1 rad/s
                                                                              Projected Gravity (nt )            ±0.1
Algorithm B.1 Stereo Depth Noise Algorithm                                    Goal Position (pt )           ±0.5 m, ±0.1 rad
Require: depth ∈ RB×H×W                                                       Observation Delay              0 ms to 600 ms
  (Kmean , Ksub ) ← C OMPUTE K ERNELS(f ilt size)
            f ·b                                                       Table C.1. Noise parameters (uniform distribution U ) applied to
  disp ← depth                                                         the actor’s observations during RL training for navigation.
  f iltered disp ← F ILTER D ISP(disp, Kmean , Ksub )
                          f ·b
  f iltered depth ← f iltered  disp
  return f iltered depth                                               with the pretraining of encoders and the use of spatial
                                                                       attention-based recurrent structures, enable robust training
   function C OMPUTE K ERNELS(s)                                       and effective sim-to-real transfer for the navigation policy.
   Compute kernel Kmean
   Compute kernel Ksub
   return (Kmean , Ksub )

   function F ILTER D ISP(disp, Kmean , Ksub )
   ρ ∼ Uniform(ρ min, ρ max)
   R ∼ BernoulliMask(shape = disp, p = ρ)
   m ← Conv2D(disp, Kmean )
   τ ∼ Uniform(τ min, τ max)
   M ← (|disp − m| < τ ) ∧ R
   v ← Quantize(disp)
   masked ← if M then v else invalid disp
   num ← Conv2D(masked, Ksub )
   den ← Conv2D(M, Ksub ) + ϵ
   f illed ← if den > 0 then num
                              den else masked
   return f illed




Prepared using sagej.cls
