<!-- GitHub profile README -->

<div align="center">
  <img src="assets/profile-banner.png" alt="Rajendar Muddasani, AI and ML Architect for post-silicon engineering" width="100%">
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/rajendar-muddasani-8a177620"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:rajendar.mi46@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-D95D39?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Role-AI%2FML_Architect-6CB4AD?style=flat-square&labelColor=163253" alt="AI and ML Architect">
  <img src="https://img.shields.io/badge/Portfolio-13_systems-F3C969?style=flat-square&labelColor=163253" alt="13 portfolio systems">
  <img src="https://img.shields.io/badge/Public_repositories-9-4EA5D9?style=flat-square&labelColor=163253" alt="9 public repositories">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/ML-Predictive_systems-F3C969?style=for-the-badge&labelColor=17222B" alt="Machine learning">
  <img src="https://img.shields.io/badge/DL-Spatial_intelligence-E56B46?style=for-the-badge&labelColor=17222B" alt="Deep learning">
  <img src="https://img.shields.io/badge/GenAI-Grounded_knowledge-4EA5D9?style=for-the-badge&labelColor=17222B" alt="Generative AI">
  <img src="https://img.shields.io/badge/Agentic_AI-Governed_workflows-9B8AFB?style=for-the-badge&labelColor=17222B" alt="Agentic AI">
</div>

## About

I am a **Senior Staff Engineer and AI/ML Architect** with 16+ years in semiconductor test engineering. I design systems that connect silicon, test, text, and engineering data to predictive models, grounded knowledge, governed agents, and human-review decisions.

This is an **evidence-first portfolio**. Public repositories use independently generated synthetic or licensed public data, bind displayed numbers to reproducible artifacts, and show limitations beside results. Confidential company code, data, identifiers, and integration details are not published.

## Evidence portfolio

The projects are ordered by the portfolio audit sequence. The **Numbers** column contains accepted evidence only; targets and architecture-only states are labelled explicitly.

| # | System | Lane | Numbers | Delivery and evidence boundary |
|---:|---|---|---|---|
| **01** | [**Post-Silicon Bin Detection MLOps**](https://github.com/rajendarmuddasani/post-silicon-bin-detection-mlops)<br>[![CI](https://github.com/rajendarmuddasani/post-silicon-bin-detection-mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/rajendarmuddasani/post-silicon-bin-detection-mlops/actions/workflows/ci.yml) | ![ML](https://img.shields.io/badge/ML-F3C969?style=flat-square&labelColor=17222B) | **15,000** synthetic dies, **25** features, **6** bins<br>Accuracy **0.8303**, macro F1 **0.5352**, ECE **0.0179** | XGBoost v4, FastAPI, Streamlit, model/schema hashing, Docker. The 20-30% test-time reduction remains a target; the strict measured policy is **0.00%**. |
| **02** | [**NLP Root Cause Predictor**](https://github.com/rajendarmuddasani/NLP_Root_Cause_Predictor)<br>[![CI](https://github.com/rajendarmuddasani/NLP_Root_Cause_Predictor/actions/workflows/ci.yml/badge.svg)](https://github.com/rajendarmuddasani/NLP_Root_Cause_Predictor/actions/workflows/ci.yml) | ![ML](https://img.shields.io/badge/ML-F3C969?style=flat-square&labelColor=17222B) | **20,000** independent synthetic reports, **10** classes<br>Accepted accuracy **88.75%** at **73.17%** coverage; OOD safe handling **97.50%** | Calibrated word/character SVM, abstention, OOD routing, feedback, drift gates, API, and containers. Real-domain approval remains pending. |
| **03** | [**RL Test Flow Optimization**](https://github.com/rajendarmuddasani/rl-test-flow-optimization)<br>[![CI](https://github.com/rajendarmuddasani/rl-test-flow-optimization/actions/workflows/ci.yml/badge.svg)](https://github.com/rajendarmuddasani/rl-test-flow-optimization/actions/workflows/ci.yml) | ![ML](https://img.shields.io/badge/ML-F3C969?style=flat-square&labelColor=17222B) | **15,000** simulated confirmation episodes<br>Defect recall **96.46%**, escapes **3.54%**, time headroom **51.30%** | Bayesian risk policy, bounded API, evidence dashboard, Docker. Experimental MaskablePPO was rejected at **82.72%** mean recall; time is simulated, not production ATE savings. |
| **04** | [**ResNet Wafer Pattern Classifier**](https://github.com/rajendarmuddasani/Transfer_Learning_ResNet_STDF_Wafer_Map_Yield_Predictor)<br>[![CI](https://github.com/rajendarmuddasani/Transfer_Learning_ResNet_STDF_Wafer_Map_Yield_Predictor/actions/workflows/ci.yml/badge.svg)](https://github.com/rajendarmuddasani/Transfer_Learning_ResNet_STDF_Wafer_Map_Yield_Predictor/actions/workflows/ci.yml) | ![DL](https://img.shields.io/badge/DL-E56B46?style=flat-square&labelColor=17222B) | **1,920 / 480 / 800** train/validation/confirmation images<br>Accuracy **93.63%**, macro F1 **0.9361**, MCC **0.9273**, minimum recall **83.0%** | Group-isolated synthetic families, ResNet-18, calibrated ONNX, FastAPI, React, Streamlit, non-root Docker. No WM-811K, STDF, yield, or production-silicon claim. |
| **05** | [**Chip-Level Test Time Optimizer**](https://github.com/rajendarmuddasani/Chip_Level_Test_Time_Optimizer) | ![DL](https://img.shields.io/badge/DL-E56B46?style=flat-square&labelColor=17222B) | **No accepted end-to-end benchmark yet**<br>15% reduction and zero escapees remain targets | Neural classifier, VAE anomaly detection, sigma rules, and conservative OR gate have architecture/component evidence. Constrained simulation is the next gate. |
| **06** | **Post-Silicon Validation RAG** | ![GenAI](https://img.shields.io/badge/GenAI-4EA5D9?style=flat-square&labelColor=17222B) | **Benchmark queued** | Private multi-format ingestion, ChromaDB, local/cloud LLM modes, and citations. Retrieval, groundedness, citation, safety, latency, and cost evidence are still required. |
| **07** | [**AARCAR Multi-Agent RCA Platform**](https://github.com/rajendarmuddasani/AARCAR-Multi-Agent-RCA-Platform) | ![Agentic AI](https://img.shields.io/badge/Agentic_AI-9B8AFB?style=flat-square&labelColor=17222B) | **Architecture and orchestration evidence**<br>No accepted RCA quality benchmark yet | Three-agent LangGraph RCA with graph analysis and semantic retrieval. Service fallbacks are disclosed; grounded RCA evaluation is the next gate. |
| **08** | [**LangGraph Multi-Agent Test Failure RCA**](https://github.com/rajendarmuddasani/LangGraph-Multi-Agent-Test-Failure-RCA-Platform) | ![Agentic AI](https://img.shields.io/badge/Agentic_AI-9B8AFB?style=flat-square&labelColor=17222B) | **Architecture and demo evidence**<br>No accepted end-to-end benchmark yet | Six-agent statistical, spatial, correlation, hypothesis, and report workflow. Real retrieval, persistence, and expert-labelled evaluation remain open. |
| **09** | [**Enterprise ML Data Pipeline**](https://github.com/rajendarmuddasani/Enterprise_ML_Data_Pipeline) | ![ML](https://img.shields.io/badge/ML-F3C969?style=flat-square&labelColor=17222B) | **Latency artifact only**<br>1,000 STDF files/day remains a target | Kafka, PySpark, Delta Lake, MLflow, Airflow, and FastAPI architecture. Safe parsing, controlled throughput, resource, lineage, and recovery evidence are required. |
| **10** | [**GraphDB GenAI MCP Test Program Development**](https://github.com/rajendarmuddasani/GraphDB_GenAI_MCP_Test_Program_Development) | ![GenAI](https://img.shields.io/badge/GenAI-4EA5D9?style=flat-square&labelColor=17222B) | **Tested starter**<br>End-to-end generation quality not yet measured | Neo4j discovery and project preflight exist. Executable MCP generation, validation fixtures, security controls, and task-quality metrics remain open. |
| **11** | **DRAM Yield Predictor MLOps** | ![DL](https://img.shields.io/badge/DL-E56B46?style=flat-square&labelColor=17222B) | **Large synthetic simulation; audit pending** | Private rare-defect Transformer-CNN with drift, canary, retraining, and rollback simulation. Metric and artifact validation plus resume-inclusion decision are required. |
| **12** | **Domain-Specific LLM Fine-Tuning Platform** | ![GenAI](https://img.shields.io/badge/GenAI-4EA5D9?style=flat-square&labelColor=17222B) | **Architecture evidence; benchmark pending** | Private LoRA/QLoRA, retrieval, evaluation APIs, and governed serving design. Public data/model selection and executed quality/safety/cost evidence remain open. |
| **13** | **ResNet U-Net Wafer Map Defect Segmenter** | ![DL](https://img.shields.io/badge/DL-E56B46?style=flat-square&labelColor=17222B) | **No implementation or benchmark** | Private empty repository reserved for a distinct pixel-level segmentation project. Build-versus-archive decision is required before presentation. |

## Architecture method

```mermaid
flowchart LR
    A[Post-silicon question] --> B[Data and provenance]
    B --> C[ML, DL, GenAI, or agents]
    C --> D[Evaluation and safety gates]
    D --> E[APIs, workflows, and review UI]
    E --> F[Human decision and feedback]
    F --> B
    style A fill:#f3c969,stroke:#17324d,color:#17324d
    style B fill:#d9efe9,stroke:#18745a,color:#17324d
    style C fill:#e56b46,stroke:#17324d,color:#ffffff
    style D fill:#9b8afb,stroke:#17324d,color:#ffffff
    style E fill:#4ea5d9,stroke:#17324d,color:#ffffff
    style F fill:#6cb4ad,stroke:#17324d,color:#17324d
```

- **Evidence:** deterministic evaluation, immutable artifacts, data/model hashes, uncertainty, and measured-versus-target language.
- **Model quality:** leakage controls, class-level errors, imbalance-aware metrics, calibration, shift sensitivity, and rejected experiments.
- **Operational safety:** confidence routing, bounded-risk policies, human review, drift gates, canary promotion, and rollback design.
- **Platform architecture:** APIs, containers, CI/CD, event/data platforms, retrieval, knowledge graphs, and governed agent workflows.

## Technology

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

## Contact

- [LinkedIn](https://www.linkedin.com/in/rajendar-muddasani-8a177620)
- [Email](mailto:rajendar.mi46@gmail.com)