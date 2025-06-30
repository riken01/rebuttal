# rebuttal
1. Abstract: Grammatical errors and clarity issues

Thank you for your feedback. We have thoroughly revised and checked the abstract for grammatical correctness. As elaborated in the third paragraph of the introduction, Federated Learning (FL) and Homomorphic Encryption (HE) are conventional cryptographic techniques; however, due to the nature of the prompt scenario, where we do not have control over user participation with remote models, these methods are not applicable in this context. We will clarify this further in the revised abstract.

Additionally, regarding the term "anti-adversarial," we acknowledge the need for more detailed clarification and will further elaborate on this concept in the abstract.

2. Intro: Citation and "why don't work" issues

Thank you for your comments. We have revised the introduction by including more appropriate citations that better reflect the background of LLM adoption and the associated risks. We also checked the relevance of the other citations and updated them for clarity.

For the "why don't work" issue, for the noise injection methods, the Yue et al., 2021 approach SANTEXT is included in our experiments, where we observed significant semantic distortion due to perturbations, leading to information loss. Similarly, for PII-specific encryption methods, we simulated an approach using Presidio in our experiments. The key limitation of this method is that it can only identify explicitly expressed entities, making it difficult to handle implicit sensitive information. We conducted representative experiments and case studies to analyze these methods.Regarding clustering methods, TextObfuscator in Zhou et al., 2023 generates vectors instead of actual words, which is unsuitable for our remote model scenario. We will further clarify this point in the introduction.

3. Why is the gradient magnitude needed and not just the loss?

Thank you for your insightful comment. We would like to clarify that in our approach, we indeed use the loss function to guide the optimization. As mentioned in Equation 4, we rely on the loss function to compute the objective, and the gradient is used to update the input. The reference to "gradient" was to highlight the optimization process, which adjusts the input based on the gradient of the loss function. We did not explicitly use the term "loss function" in that context, but it is the foundation of the gradient updates.

4. Experiment: 

Thank you for your comments. We appreciate your feedback on the comparison with DP-OPT and other related work such as Preempt. In the revised manuscript, we will include a comparison with DP-OPT and Preempt to clarify the positioning of our approach within the existing literature. Regarding evaluation metrics, we agree that metrics like BLEU and ROUGE are important for a comprehensive assessment. In the revised experiments section, we will include these metrics as part of our evaluation.

1. Masking Ablation

Thank you for your comment. While the accuracy improvement may seem marginal and MTI top-1 slightly worse, we believe that our approach offers a more comprehensive improvement in privacy and utility. Our masking technique is specifically designed to reduce the inference of implicit privacy rather than focusing purely on accuracy or MTI.

As detailed in Appendix A.1, PersonalPortrait dataset includes Occupation annotations—a sensitive, implicit privacy attribute that can be inferred from context. In our PII testing, we observed that using TF-IDF masking provided a more effective privacy-preserving strategy, showing better results in reducing the inference of Occupation compared to other approaches. The below table shows the result.

| PI{Occ.} | Random Masking | PromptObfus |
|----------|----------------|-------------|
| k = 0.1  | 44.50          | 45.75       |
| k = 0.2  | 43.25          | 37.75       |
| k = 0.3  | 34.75          | 17.25       |


We will update the manuscript to more clearly explain the trade-off between utility and privacy, and to highlight the advantages of our method in handling implicit privacy attributes.


   
1. Gradient Ablation

As explained in Section 3.3, Paragraphs 4 and 5, our method does not simply select the gradients with the smallest magnitude. We also perform additional filtering to exclude not only those gradients but also any words that are either identical to the original words or are synonyms. This careful selection process helps preserve privacy while still improving the MTI and EI metrics. Top-1 and random filtering methods may select words that could potentially leak sensitive information. We will provide a more detailed explanation of this filtering strategy in the experiments section to better clarify why our approach offers an effective privacy-utility balance.
