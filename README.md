[Label Efficient Learning of Transferable Representations Across Domains and Tasks](6621-label-efficient-learning-of-transferable-representations-acrosss-domains-and-tasks.pdf)


## TLDR;


## NOTES

### TODO
1. Process the MNIST and SVNH Dataset as required: Crudely Done
  * MNIST : 5-9 Classes - Done
  * SVNH : 0-4 Classes - Done
2. Creation of Architecture as shown in the image : ![architecture](https://github.com/Gokkulnath/Research-Paper-Result-Reproduction/blob/master/Domain%20Adaptaion%20in%20Video/ARchitecture%20-%20Copy.PNG) - Keras Issue - Need Debugging
3. Train the Model with Optimiser Specified Separately and load the weights in the main experiment.
4. Initialise Weights only for Source CNN Model with the pretrained weights.
5. Proceed with Trainning the Entire Architecture.



# Six different methods : 
* (i) Target only: the model is trained on D2 from scratch; 
* (ii) Fine-tune: the model is pretrained on D1 and fine-tuned on D2;
* (iii) Matching networks [70]: we first pretrain the model on D3, then use D2 as the support set in the matching networks; 
* (iv) Fine-tuned matching networks: same as baseline iii, except that for each k the model is fine-tuned on D2 with 5-way (k 􀀀 1)-shot learning: k 􀀀 1 examples in each class are randomly selected as the support set, and the last example in each class is used as the query set; 
* (v) Fine-tune + adversarial: in addition to baseline ii, the model is also trained on D1 and D3 with a domain adversarial loss; 
* (vi.) Full model: fine-tune the model with the proposed multi-layer domain adversarial loss.




# Module : # TO DO:
Softmax with Temperature