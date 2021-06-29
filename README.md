# ASSIST (Alcoholism Solutions: Synthesizing Information to Support Treatments)

This repo contains the source code of ASSIST analysis modules developed under the Phase I of the ASSIST project. These modules can be run in Jupyter notebooks, Docker containers, as well as workflows managed by the ADE (Active Discovery Engine) with increasing support for provenance.

### Description of analysis modules:
| Analysis Module | Description |
|-------|-------------|
| Network Analysis | <brief description> |
| Module Extraction | <brief description> |
| Module Membership Analysis | <brief description> |
| Module DE/Diagnostic Correlation | <brief description> |
| Module Network Embedding |<brief description> |
| ML and Critical Gene Identifier | <brief description> |

The above analysis modules are inter-related as depicted in the conceptual workflow below.
<p align="center">
  <img src="https://user-images.githubusercontent.com/12038408/117026434-ca74fa80-acc9-11eb-937c-ffaa7547ff34.png" width="700" height="650">
</p>

Module ```Critical Gene Validation``` (brief description) requires a 3rd party license and is thus not included in this repo.

## User Guide

Below we describe how to set up and run the ASSIST analysis modules in three different modes.


To run ASSIST software on your machine, you need to have Java, Python and Docker installed. We recommend Java SE Runtime 15.0.2, Python 3.7+ (tested on 3.8.5) and Docker 20.10.6. GNU Make 3.81 is also required to build the Docker images. Below we describe how to set up and run the ASSIST analysis modules in three different modes.


### 1. How to set up the environment for Jupyter notebooks
Jupyter notebooks for ASSIST analysis modules are included to allow researchers to test out the analysis code using the Jupyter notebook interface.

### 2. How to launch containers for each analysis module

### 3. How to run ASSIST modules in a workflow using ADE

#### Prepare ADE runtime environment

#### Create a workflow module in ADE

#### Integrate workflow modules in ADE

#### How to navigate in ADE


For each of the analysis modules below, include detailed description on input data (file name, file content, columns the module cares about), what the analysis does about the input data, and what the output the module generates. This can include snapshots of sample dataframes and plots.

**Network Analysis**

**Module Extraction**

**Module Membership Analysis**

**Module DE/Diagnostic Correlation**

**Module Network Embedding**


**ML and Critical Gene Identifier**

<table border="1">
    <thead>
        <tr>
            <th></th>
            <th><sub>File</sub></th>
            <th><sub>Description</sub></th>
            <th><sub>Human</sub></th>
            <th><sub>Mouse</sub></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=5><sub>Input</sub></td>
            <td><sub>Kapoor_TOM.csv</sub></td>
            <td><sub>TOM co-expression network</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub></sub></td>
        </tr>
        <tr>
            <td><sub>embedding.csv</sub></td>
            <td><sub>network embedding</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
        <tr>
            <td><sub>expression_meta.csv</sub></td>
            <td><sub>normalized expression data joined with subjects' metadata</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub></sub></td>
        </tr>
        <tr>
            <td><sub>deseq.alc.vs.control.age.rin.batch.gender.PMI. corrected.w.prot.coding.gene.name.xlsx</sub></td>
            <td><sub>differential expression analysis</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub></sub></td>
        </tr>
        <tr>
            <td><sub>de_data.csv</sub></td>
            <td><sub>differential expression analysis</sub></td>
            <td><sub></sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td rowspan=9><sub>Output</sub></td>
            <td><sub>critical_genes.csv</sub></td>
            <td><sub>candidate genes identified by ASSIST</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
        <tr>
            <td><sub>neighbor_genes.csv</sub></td>
            <td><sub>closest DEG neighbors in the co-expression network</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
        <tr>
            <td><sub>run_ml_.png</sub></td>
            <td><sub>machine learning accuracy</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
        <tr>
            <td><sub>run_ml_top_dims.png</sub></td>
            <td><sub>machine learning accuracy using only the most important dimensions</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
        <tr>
            <td><sub>gene_phenotype_corr_for_xx.png</sub></td>
            <td><sub>critical gene/DEG/neighbor gene correlation with alcohol traits</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub></sub></td>
        </tr>
        <tr>
            <td><sub>alcohol trait correlation CG, neighbor & DEG.png</sub></td>
            <td><sub>distribution plot to compare gene_phenotype_corr_for_xx.png</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub></sub></td>
        </tr>
        <tr>
            <td><sub>jaccard_average_Important dim overlap within model repeats.png</sub></td>
            <td><sub>the important dimensions overlap between the repeats of each model</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
        <tr>
            <td><sub>jaccard_critical_genes_Critical gene overlap between models.png</sub></td>
            <td><sub>critical gene overlap between each two models</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
        <tr>
            <td><sub>plot_nearby_impact_num_.png</sub></td>
            <td><sub>top 10 critical genes</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
            <td><sub>:heavy_check_mark:</sub></td>
        </tr>
    </tbody>
</table>

## Questions?
Please contact Yi-Pei Chen (ychen@netrias.com) or George Zheng (gzheng@netrias.com)
