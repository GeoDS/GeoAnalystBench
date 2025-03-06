# GeoAnalystBench
GeoAnalystBench: A GeoAI benchmark for assessing large language models for spatial analysis workflow and code generation

## Automating GIS Workflows with Large Language Models (LLMs)


Recent advances in Geospatial Artificial Intelligence (GeoAI) have been driven by generative AI and foundation models. While powerful geoprocessing tools are widely available in Geographic Information Systems (GIS), automating these workflows using AI-driven Python scripting remains a challenge, especially for non-expert users.

This project explores the capabilities of Large Language Models (LLMs) such as ChatGPT, Claude, Gemini, Llama, and DeepSeek in automating GIS workflows. We introduce a benchmark of 50 geoprocessing tasks to evaluate these models' ability to generate Python functions from natural language instructions.

Our findings reveal that proprietary LLMs achieve higher success rates (>90%) and produce workflows more aligned with human-designed implementations than open-source models. The results suggest that integrating proprietary LLMs with ArcPy is a more effective approach for specialized GIS workflows.

By providing benchmarks and insights, this study contributes to the development of optimized prompting strategies, future GIS automation tools, and hybrid GeoAI workflows that combine LLMs with human expertise.
![GeoAnalystBench](./figures/framework.png)
## Key Features:
- **Benchmark for GIS Automation**: Evaluation of LLMs on 50 geoprocessing tasks.
- **LLM Performance Comparison**: Validity and similarity analysis of generated workflows.
- **Open-source Versus Proprietary Models**: Comparison of performance and reliability.

## Dataset

This research developed 50 Python-based geoprocessing tasks derived
from GIS platforms, software, online tutorials, and academic literature. Each task comprises 3 to 10 subtasks, because
the simplest task still involves data loading, applying at least one spatial analysis tool, and saving the final outputs. The
list of those tasks with their sources are included in the [Tasks](#tasks) section below.

The dataset includes the following information:
| Key Column                | Description |
|---------------------------|-------------|
| ID                        | Unique identifier for each task |
| Open or Closed Source     | Use open source or closed source library |
| Task                      | Brief description of the task |
| Instruction               | Natural language instruction for completing the task |
| Domain Knowledge          | Domain-specific knowledge related to task |
| Dataset Description       | Data name, format, descriptions, and key columns |
| Human Designed Workflow   | Numbered list of human-designed workflow |
| Task Length               | The length of the human-designed workflow |
| Code                      | Human-designed code for the task and dataset |

The dataset is avaliable to download at [GeoAnalystBench](https://github.com/GeoDS/GeoAnalystBench/blob/master/dataset/GeoAnalystBench.csv).

The data being used in this research is avaliable to download at (tbd).

## Tasks
There are 50 tasks in the dataset, and this section covers all tasks and their sources. For more details, please refer to the [GeoAnalystBench](https://github.com/GeoDS/GeoAnalystBench/blob/master/dataset/GeoAnalystBench.csv).

Note that there are tasks with the same name but different id. This typically happens when the task is slightly different, or the task is a subset of a larger task.

<details>
  <summary>Click to expand/collapse Task List</summary>

  | ID | Task Name | Source |
  |----|-----------|--------|
  | 1  | Find heat islands and at-risk populations in Madison, Wisconsin | [Analyze urban heat using kriging](https://learn.arcgis.com/en/projects/analyze-urban-heat-using-kriging/) |
  | 2  | Find future bus stop locations in Hamilton | [Assess access to public transit](https://learn.arcgis.com/en/projects/assess-access-to-public-transit/) |
  | 3  | Assess burn scars and wildfire impact in Montana using satellite imagery | [Assess burn scars with satellite imagery](https://learn.arcgis.com/en/projects/assess-burn-scars-with-satellite-imagery/) |
  | 4  | Identify groundwater vulnerable areas that need protection | [Identify groundwater vulnerable areas](https://learn.arcgis.com/en/projects/identify-groundwater-vulnerable-areas/) |
  | 5  | Visualize data on children with elevated blood lead levels while protecting privacy | [De-identify health data for visualization and sharing](https://learn.arcgis.com/en/projects/de-identify-health-data-for-visualization-and-sharing/) |
  | 6  | Use animal GPS tracks to model home range and movement over time | [Model animal home range](https://learn.arcgis.com/en/projects/model-animal-home-range/) |
  | 7  | Analyze the impacts of land subsidence on flooding | [Model how land subsidence affects flooding](https://learn.arcgis.com/en/projects/model-how-land-subsidence-affects-flooding/) |
  | 8  | Find gaps in Toronto fire station service coverage | [Get started with Python in ArcGIS Pro](https://learn.arcgis.com/en/projects/get-started-with-python-in-arcgis-pro/) |
  | 9  | Find the deforestation rate for Rondônia | [Predict deforestation in the Amazon rain forest](https://learn.arcgis.com/en/projects/predict-deforestation-in-the-amazon-rain-forest/) |
  | 10 | Analyze the impact of proposed roads on the local environment | [Predict deforestation in the Amazon rain forest](https://learn.arcgis.com/en/projects/predict-deforestation-in-the-amazon-rain-forest/) |
  | 11 | Create charts in Python to explore coral and sponge distribution around Catalina Island | [Chart coral and sponge distribution](https://learn.arcgis.com/en/projects/chart-coral-and-sponge-distribution-factors-with-python/) |
  | 12 | Find optimal corridors to connect dwindling mountain lion populations | [Build a model to connect mountain lion habitat](https://learn.arcgis.com/en/projects/build-a-model-to-connect-mountain-lion-habitat/) |
  | 13 | Understand the relationship between ocean temperature and salinity at various depths in the South Atlantic Ocean | [SciTools Iris](https://github.com/SciTools/iris) |
  | 14 | Detect persistent periods of high temperature over the past 240 years | [SciTools Iris](https://github.com/SciTools/iris) |
  | 15 | Understand the geographical distribution of Total Electron Content (TEC) in the ionosphere | [SciTools Iris](https://github.com/SciTools/iris) |
  | 16 | Analyze climate change trends in North America using spatiotemporal data | [SciTools Iris](https://github.com/SciTools/iris) |
  | 17 | Analyze the geographical distribution of fatal car crashes in New York City during 2016 | [NYC Crash Data](https://github.com/ResidentMario/geoplot/blob/master/examples/plot_nyc_collisions_map.py) |
  | 18 | Analyze street tree species data in San Francisco | [San Francisco Tree Data](https://github.com/ResidentMario/geoplot/blob/master/examples/plot_san_francisco_trees.py) |
  | 19 | Model spatial patterns of water quality | [Model water quality](https://learn.arcgis.com/en/projects/model-water-quality-using-interpolation/) |
  | 20 | Predict the likelihood of tin-tungsten deposits in Tasmania | [Solve Geosolutions](https://github.com/Solve-Geosolutions/transform_2022) |
  | 21 | Find optimal corridors to connect dwindling mountain lion populations(2) | [Build a model to connect mountain lion habitat](https://learn.arcgis.com/en/projects/build-a-model-to-connect-mountain-lion-habitat/) |
  | 22 | Find optimal corridors to connect dwindling mountain lion populations(3) | [Build a model to connect mountain lion habitat](https://learn.arcgis.com/en/projects/build-a-model-to-connect-mountain-lion-habitat/) |
  | 23 | Assess Open Space to Lower Flood Insurance Cost | [Assess open space to lower flood insurance cost](https://learn.arcgis.com/en/projects/assess-open-space-to-lower-flood-insurance-cost/) |
  | 24 | Provide a de-identified point-level dataset that includes all the variables of interest for each child, as well as their general location | [De-identify health data for visualization and sharing](https://learn.arcgis.com/en/projects/de-identify-health-data-for-visualization-and-sharing/) |
  | 25 | Create risk maps for transmission, susceptibility, and resource scarcity. Then create a map of risk profiles to help pinpoint targeted intervention areas | [Analyze COVID-19 risk using ArcGIS Pro](https://learn.arcgis.com/en/projects/analyze-covid-19-risk-using-arcgis-pro/) |
  | 26 | Use drainage conditions and water depth to calculate groundwater vulnerable areas | [Identify groundwater vulnerable areas](https://learn.arcgis.com/en/projects/identify-groundwater-vulnerable-areas/) |
  | 27 | Identify undeveloped areas from groundwater risk zones | [Identify groundwater vulnerable areas](https://learn.arcgis.com/en/projects/identify-groundwater-vulnerable-areas/) |
  | 28 | Estimate the origin-destination (OD) flows between regions based on the socioeconomic attributes of regions and the mobility data | [ScienceDirect - OD Flow Estimation](https://www.sciencedirect.com/science/article/pii/S2210670724008382) |
  | 29 | Calculate Travel Time for a Tsunami | [Calculate travel time for a tsunami](https://learn.arcgis.com/en/projects/calculate-travel-time-for-a-tsunami/) |
  | 30 | Designate bike routes for commuting professionals | [Designate bike routes](https://desktop.arcgis.com/en/analytics/case-studies/designate-bike-routes-for-commuters.htm) |
  | 31 | Detect aggregation scales of geographical flows | [Geographical Flow Aggregation](https://www.tandfonline.com/doi/full/10.1080/13658816.2020.1749277) |
  | 32 | Find optimal corridors to connect dwindling mountain lion populations | [Build a model to connect mountain lion habitat](https://learn.arcgis.com/en/projects/build-a-model-to-connect-mountain-lion-habitat/) |
  | 33 | Analyze the impacts of land subsidence on flooding | [Model how land subsidence affects flooding](https://learn.arcgis.com/en/projects/model-how-land-subsidence-affects-flooding/) |
  | 34 | Estimate the accessibility of roads to rural areas in Japan | [Estimate access to infrastructure](https://learn.arcgis.com/en/projects/estimate-access-to-infrastructure/) |
  | 35 | Calculate landslide potential for communities affected by wildfires | [Landslide Potential Calculation](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/overview-of-spatial-analyst.htm) |
  | 36 | Compute the change in vegetation before and after a hailstorm with the SAVI index | [Assess hail damage in cornfields with satellite imagery](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/ndvi.htm) |
  | 37 | Analyze human sentiments of heat exposure using social media data | [iGuide Notebook](https://platform.i-guide.io/notebooks/6c518fed-0a65-4858-949e-24ee8dc4d85b) |
  | 38 | Calculate travel time from one location to others in a neighborhood | [iGuide Notebook](https://platform.i-guide.io/notebooks/02f9b712-f4ac-47bc-9382-3c1e0f37b4e3) |
  | 39 | Train a Geographically Weighted Regression model to predict Georgia's Bachelor's degree rate | [iGuide Notebook](https://platform.i-guide.io/notebooks/d8926bb3-864d-4542-8027-02fc6edc868f) |
  | 40 | Calculate and visualize changes in malaria prevalence | [Visualizing Shrinking Malaria Rates](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/visualize-shrinking-malaria-rates-in-africa/) |
  | 41 | Improve campsite data quality using a relationship class | [Improve campsite data](https://learn.arcgis.com/en/projects/improve-campsite-data-quality-using-a-relationship-class/) |
  | 42 | Investigate spatial patterns for Airbnb prices in Berlin | [Determine dangerous roads for drivers](https://learn.arcgis.com/en/projects/determine-the-most-dangerous-roads-for-drivers/) |
  | 43 | Use animal GPS tracks to model home range to understand where they are and how they move over time | [Model animal home range](https://learn.arcgis.com/en/projects/model-animal-home-range/) |
  | 44 | Find gap for Toronto fire station service coverage | [Get started with Python in ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) |
  | 45 | Find optimal corridors to connect dwindling mountain lion populations | [Build a model to connect mountain lion habitat](https://learn.arcgis.com/en/projects/build-a-model-to-connect-mountain-lion-habitat/) |
  | 46 | Identify hot spots for peak crashes | [Determine the most dangerous roads for drivers](https://learn.arcgis.com/en/projects/determine-the-most-dangerous-roads-for-drivers/) |
  | 47 | Calculate impervious surface area | [Calculate impervious surfaces](https://learn.arcgis.com/en/projects/calculate-impervious-surfaces-from-spectral-imagery/) |
  | 48 | Determine how location impacts interest rates | [Impact of Location on Interest Rates](https://learn.arcgis.com/en/projects/determine-how-location-impacts-interest-rates/) |
  | 49 | Mapping the Impact of Housing Shortage on Oil Workers | [Homeless in the Badlands](https://learn.arcgis.com/en/projects/homeless-in-the-badlands/arcgis-pro/) |
  | 50 | Predict seagrass habitats | [Predict seagrass habitats with machine learning](https://learn.arcgis.com/en/projects/predict-seagrass-habitats-with-machine-learning/#prepare-training-data) |
</details>



## Case Study 1

## Case Study 2


## Reference

