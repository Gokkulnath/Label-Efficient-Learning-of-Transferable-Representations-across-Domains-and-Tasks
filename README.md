# Label Efficient Learning of Transferable Representations across Domains and Tasks


TLDR: Learn a representation that is transferable across different domains and tasks in a data efficient manner. The framework is trained jointly to minimize the domain shift, to transfer knowledge to new task, and to learn from large amounts of unlabeled data.


**Idea:** Given a large labeled source dataset with annotations for a task set  A, we seek to transfer knowledge to a sparsely labeled target domain with a possibly wholly new task set B.

**Intuition:** We should be able to learn reusable and general purpose representations which enable faster learning of future tasks requiring less human intervention

**Proposed Solution:** Jointly adapt a source representation for use in a distinct target domain using a new multi layer unsupervised domain adversarial formulation while introducing a novel cross-domain and within domain class similarity objective. This new objective can be applied even when the target domain has non-overlapping classes to the source domain.

**Evaluation:** Evaluate our approach in the challenging setting of joint transfer across domains and tasks and demonstrate our ability to successfully transfer, reducing the need for annotated data for the target domain and tasks.


## Concepts


- Domain adaptation: Domain adaptation seeks to learn a well  performing model [related to source domains] on target data distribution. 

- Few-shot learning:



### TODO 

Code Walk-through:
    - [x] Dataset and Data-loader Preparation
    - [ ] Preparing Baselines 
      - [ ] Target only: the model is trained on D2 from scratch;
      - [ ] Fine-tune: the model is pretrained on D1 and fine-tuned on D2;
      - [ ] Matching networks [70]: we first pretrain the model on D3, then use D2 as the support set in the matching networks;
      - [ ] Fine-tuned matching networks: same as baseline iii, except that for each k the model is  fine-tuned on D2 with 5-way (k 􀀀 1)-shot learning: k 􀀀 1 examples in each class are randomly selected as the support set, and the last example in each class is used as the query set;
      - [ ] Fine-tune + adversarial: in addition to baseline ii, the model is also trained on D1 and D3 with a domain adversarial loss;
      - [ ] Full model: fine-tune the model with the proposed multi-layer domain adversarial loss.

Understanding Experiment and its Hyper parameter
Experiment: 1  -> Transferring from a subset of SVHN containing only digits 0-4 to a subset of MNIST  containing only digits 5-9.

Experiment: 2  -> Adapting From ImageNet [6] object-centric images to UCF-101 [57] videos for action recognition. [Not Done to Compute Limitations]

