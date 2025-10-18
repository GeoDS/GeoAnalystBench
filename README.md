# GeoAnalystBench
GeoAnalystBench: A GeoAI benchmark for assessing large language models for spatial analysis workflow and code generation

## Automating GIS Workflows with Large Language Models (LLMs)

## Reference

Zhang, Q., Gao, S., Wei, C., Zhao, Y., Nie, Y., Chen, Z., Chen, S., Su, Y., & Sun, H. (2025). [GeoAnalystBench: A GeoAI benchmark for assessing large language models for spatial analysis workflow and code generation.](https://onlinelibrary.wiley.com/doi/10.1111/tgis.70135) Transactions in GIS, 29(7), e70135.


```
@article{zhang2025geoanalystbench,
  title={GeoAnalystBench: A GeoAI benchmark for assessing large language models for spatial analysis workflow and code generation},
  author={Zhang, Qianheng and Gao, Song and Wei, Chen and Zhao, Yibo and Nie, Ying and Chen, Ziru and Chen, Shijie and Su, Yu and Sun, Huan},
  journal={Transactions in GIS},
  volume={29},
  number={7},
  pages={e70135},
  year={2025}
}
```

Recent advances in Geospatial Artificial Intelligence (GeoAI) have been driven by generative AI and foundation models. While powerful geoprocessing tools are widely available in Geographic Information Systems (GIS), automating these workflows using AI-driven Python scripting remains a challenge, especially for non-expert users.

This project explores the capabilities of Large Language Models (LLMs) such as ChatGPT, Claude, Gemini, Llama, and DeepSeek in automating GIS workflows. We introduce a benchmark of well-designed 50 real-world geoprocessing tasks carefully validated by GIS domain experts to evaluate these models' ability to generate Python functions from natural language instructions.

Our findings reveal that proprietary LLMs achieve higher success rates (>90%) and produce workflows more aligned with human-designed implementations than smaller parameter-sized open-source models. The results suggest that integrating proprietary LLMs with ArcPy is a more effective approach for specialized GIS workflows.

By providing benchmarks and insights, this study contributes to the development of optimized prompting strategies, future GIS automation tools, and hybrid GeoAI workflows that combine LLMs with human expertise.
![GeoAnalystBench](./figures/framework.png)
## Key Features:
- **Benchmark for GIS Automation**: Evaluation of LLMs on 50 real-world geoprocessing tasks.
- **LLM Performance Comparison**: Validity and similarity analysis of generated workflows.
- **Open-source Versus Proprietary Models**: Comparison of performance and reliability.

## Dataset

This research developed 50 Python-based real-world geoprocessing tasks derived
from GIS platforms, software, online tutorials, and academic literature. Each task comprises 3 to 10 subtasks, because
the simplest task still involves data loading, applying at least one spatial analysis tool, and saving the final outputs. The
list of those tasks with their sources are included in the [Tasks](#tasks) section below.

The geoprocessing task dataset includes the following information:
| Key Column                | Description |
|---------------------------|-------------|
| ID                        | Unique identifier for each task |
| Open or Closed Source     | Use open source or closed source library |
| Task                      | Brief description of the task |
| Instruction/Prompt        | Natural language instruction for completing the task |
| Domain Knowledge          | Domain-specific knowledge related to task |
| Dataset Description       | Data name, format, descriptions, and key columns |
| Human Designed Workflow   | Numbered list of human-designed workflow |
| Task Length               | The length of the human-designed workflow |
| Code                      | Human-designed Python code for the task and dataset |

The geoprocessing task dataset is avaliable to download at [GeoAnalystBench](https://github.com/GeoDS/GeoAnalystBench/blob/master/dataset/GeoAnalystBench.csv).

The data being used in this research is avaliable to download at [Google Drive](https://drive.google.com/drive/u/0/folders/1GhgxWkNVh4FTgS1RETgvbstBqx0Q9ezp).

## Tasks
There are 50 tasks in the dataset, and this section covers all tasks and their sources. For more details, please refer to the [GeoAnalystBench](https://github.com/GeoDS/GeoAnalystBench/blob/master/dataset/GeoAnalystBench.csv).

Note that there are tasks with the same name but different id. This typically happens when the task is slightly different, or the task is a subset of a larger task.

<!-- <details>
  <summary>Click to expand/collapse Task List</summary> -->

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
  | 17 | Analyze the geographical distribution of fatal car crashes in New York City during 2016 | [Pointplot of NYC fatal and injurious traffic collisions](https://github.com/ResidentMario/geoplot/blob/master/examples/plot_nyc_collisions_map.py) |
  | 18 | Analyze street tree species data in San Francisco | [Quadtree of San Francisco street trees](https://github.com/ResidentMario/geoplot/blob/master/examples/plot_san_francisco_trees.py) |
  | 19 | Model spatial patterns of water quality | [Model water quality](https://learn.arcgis.com/en/projects/model-water-quality-using-interpolation/) |
  | 20 | Predict the likelihood of tin-tungsten deposits in Tasmania | [Geospatial ML Challenges: A prospectivity analysis example](https://github.com/Solve-Geosolutions/transform_2022) |
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
  | 37 | Analyze human sentiments of heat exposure using social media data | [National-level Analysis using Twitter Data](https://platform.i-guide.io/notebooks/6c518fed-0a65-4858-949e-24ee8dc4d85b) |
  | 38 | Calculate travel time from one location to others in a neighborhood | [Intro to OSM Network Data](https://platform.i-guide.io/notebooks/02f9b712-f4ac-47bc-9382-3c1e0f37b4e3) |
  | 39 | Train a Geographically Weighted Regression model to predict Georgia's Bachelor's degree rate | [Geographically Weighted Regression Demo](https://platform.i-guide.io/notebooks/d8926bb3-864d-4542-8027-02fc6edc868f) |
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
<!-- </details> -->



## Case Study 1 (Task 43): Identification of Home Range and Spatial Clusters from Animal
Movements
Understanding elk movement patterns is critical for wildlife conservation and management in the field of animal ecology. The task needs to identify elk home ranges in Southwestern Alberta, 2009 using GPS-tracking locations. In doing so, researchers are able to analyze their space use and movement clusters for elk populations. Understanding the home range of the elk population is essential for ensuring sustainability and stability of the wildlife.

![elk](case_study/figures/elk.png)

### Dataset
• berling_neighbourhoods.geojson: Geojson file for multipolygons of neighbourhoods in Berling, properties include "neighbourhood" and "neighbourhood_group".

• berlin-listings.csv: CSV file of Berling Airbnb information, with lat and lng of Airbnb.


### Prompts
<details>
  <summary>Click to expand/collapse Workflow Prompts</summary>

  >  As a Geospatial data scientist, you will generate a workflow to a proposed task.
  >
  >  [Task]:
  >  Use animal GPS tracks to model home range to understand where they are and how they move over time.
  >
  >  [Instruction]:
  >  Your task is to analyze and visualize elk movements using the provided dataset. The goal is to estimate
  >  home ranges and assess habitat preferences using spatial analysis techniques, including Minimum
  >  Bounding Geometry (Convex Hull), Kernel Density Estimation, and Density-Based Clustering (DBSCAN).
  >  The analysis will generate spatial outputs stored in "dataset/elk_home_range.gdb" and "dataset/".
  >
  >  [Domain Knowledge]:
  >  "Home range" can be defined as the area within which an animal normally lives and finds what it needs
  >  for survival. Basically, the home range is the area that an animal travels for its normal daily activities.
  >  "Minimum Bounding Geometry" creates a feature class containing polygons which represent a specified
  >  minimum bounding geometry enclosing each input feature or each group of input features. "Convex
  >  hull" is the smallest convex polygon that can enclose a group of objects, such as a group of points.
  >  "Kernel Density Mapping" calculates and visualizes features's density in a given area. "DBSCAN",
  >  Density-Based Spatial Clustering of Applications with Noise that cluster the points based on density
  >  criterion.
  >  [Dataset Description]:
  >  dataset/Elk_in_Southwestern_Alberta_2009.geojson: geojson files for storing points of Elk
  >  movements in Southwestern Alberta 2009.
  >
  >  Columns of dataset/Elk_in_Southwestern_Alberta_2009.geojson:
  >  'OBJECTID', 'timestamp', 'long', 'lat', 'comments', 'external_t', 'dop',
  >  'fix_type_r', 'satellite_', 'height', 'crc_status', 'outlier_ma',
  >  'sensor_typ', 'individual', 'tag_ident', 'ind_ident', 'study_name',
  >  'date', 'time', 'timestamp_Converted', 'summer_indicator', 'geometry'
  >
  >
  >  [Key Notes]:
  >  1.Use **automatic reasoning** and clearly explain each step (Chain of Thoughts approach).
  >
  >  2.Using **NetworkX* package for visualization.
  >
  >  3.Using 'dot' for graph visualization layout.
  >
  >  4.Multiple subtasks can be proceeded correspondingly because
  >  all of their outputs will be inputs for the next subtask.
  >
  >  5.Limiting your output to code, no extra information.
  >
  >  6.Only codes for workflow, no implementation.
  >
  >  [Expected Sample Output Begin]
  >
  >  """
  >
  >    tasks = [Task1, Task2, Task3]
  >
  >    G = nx.DiGraph()
  >
  >  for i in range(len(tasks) - 1):
  >
  >    G.add_edge(tasks[i], tasks[i + 1])
  >
  >    pos = nx.drawing.nx_pydot.graphviz_layout(G, prog="dot")
  >
  >    plt.figure(figsize=(15, 8))
  >
  >    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
  >
  >    plt.title("Workflow for Analyzing Urban Heat Using Kriging Interpolation", fontsize=14)
  >
  >    plt.show()
  >
  >  """
  >
  >  [Expected Sample Output End]
</details>

<details>
  <summary>Click to expand/collapse Code Generation Prompts</summary>

> As a Geospatial data scientist, generate a python file to solve the proposed task.
>
> [Task]:
> Use animal GPS tracks to model home range to understand where they are and how they move over time.
>
> [Instruction]:
> Your task is to analyze and visualize elk movements using the provided dataset. The goal is to estimate
> home ranges and assess habitat preferences using spatial analysis techniques, including Minimum
> Bounding Geometry (Convex Hull), Kernel Density Estimation, and Density-Based Clustering (DBSCAN).
> The analysis will generate spatial outputs stored in ""dataset/elk_home_range.gdb"" and ""dataset/"".
>
> [Domain Knowledge]:
> "Home range" can be defined as the area within which an animal normally lives and finds what it needs
> for survival. Basically, the home range is the area that an animal travels for its normal daily activities.
>
> "Minimum Bounding Geometry" creates a feature class containing polygons which represent a specified
> minimum bounding geometry enclosing each input feature or each group of input features.
>
> "Convex hull" is the smallest convex polygon that can enclose a group of objects, such as a group of points.
>
> "Kernel Density Mapping" calculates and visualizes features's density in a given area. "DBSCAN",
> Density-Based Spatial Clustering of Applications with Noise that cluster the points based on density
> criterion.
>
> [Dataset Description]:
> dataset/Elk_in_Southwestern_Alberta_2009.geojson: geojson files for storing points of Elk
> movements in Southwestern Alberta 2009.
>
> Columns of dataset/Elk_in_Southwestern_Alberta_2009.geojson:
> 'OBJECTID', 'timestamp', 'long', 'lat', 'comments', 'external_t', 'dop',
> 'fix_type_r', 'satellite_', 'height', 'crc_status', 'outlier_ma',
> 'sensor_typ', 'individual', 'tag_ident', 'ind_ident', 'study_name',
> 'date', 'time', 'timestamp_Converted', 'summer_indicator', 'geometry'
>
>
>
> [Key Notes]:
> 1.Use **automatic reasoning** and clearly explain each subtask before performing it (ReAct approach).
>
> 2.Using latest python packages for code generation
>
> 3.Put all code under main function, no helper functions
>
> 4.Limit your output to code, no extra information.
>
> 5.Use latest **Arcpy** functions only
"

</details>

### Results
<p align="center">
  <img src="case_study/figures/ElkAI.png" alt="elk">
</p>

## Case Study 2 (Task 46): Spatial Hotspot Analysis of Car Accidents
The second case study is about spatial hotspot analysis of car accidents. The Brevard County in Florida has one of the
deadliest interstate highways in the United States. This case study aims to identify the spatially distributed hot spots
along the road network. The dataset includes road network, crash locations from 2010 to 2015, and a network spatial
weighting matrix. Understanding the hot spots for car accidents is essential for the local transportation department
to make policies and quick responses for future accidents.

![hotspot](case_study/figures/traffic.png)
### Dataset
• roads.shp: The road network of Brevard County.

• crashes.shp: The locations of crashes in Brevard County, Florida between 2010 and 2015.

• nwswm360ft.swm: Spatial weights matrix file created using the Generate Network Spatial Weights tool and a street network built from Brevard County road polylines.


### Prompts
<details>
  <summary>Click to expand/collapse Workflow Prompts</summary>

  > As a Geospatial data scientist, you will generate a workflow to a proposed task.

  > [Task]:
  > Identify hot spots for peak crashes
  >
  > [Instruction]:
  > Your task is identifying hot spots for peak crashes in Brevard County, Florida, 2010 - 2015. The first
  > step is select all the crashes based on peak time zone. Create a copy of selected crashes data. Then,
  > snap the crashes points to the road network and spatial join with the road. Calculate the crash rate
  > based on the joint data and use hot spot analysis to get crash hot spot map as the result.
  >
  > [Domain Knowledge]:
  > We consider traffic between time zone 3pm to 5pm in weekdays as peak. For snap process, the recommend
  > buffer on roads is 0.25 miles. Hot spot analysis looks for high crash rates that cluster close together,
  > accurate distance measurements based on the road network are essential.
  >
  > [Dataset Description]:
  > dataset/crashes.shp: The locations of crashes in Brevard County, Florida between 2010 and 2015.

  > dataset/roads.shp: The road network of Brevard County.
  >
  > dataset/nwswm360ft.swm: Spatial weights matrix file created using the Generate Network Spatial
  >
  > Weights tool and a street network built from Brevard County road polylines.

  > [Key Notes]:
  > 1.Use **automatic reasoning** and clearly explain each step (Chain of Thoughts approach).
  >
  > 2.Using **NetworkX* package for visualization.
  >
  > 3.Using 'dot' for graph visualization layout.
  >
  > 4.Multiple subtasks can be proceeded correspondingly because
  > all of their outputs will be inputs for the next subtask.
  >
  > 5.Limiting your output to code, no extra information.
  >
  > 6.Only codes for workflow, no implementation.

  >[Expected Sample Output Begin]

  >"""
  >
  > tasks = [Task1, Task2, Task3]

  > G = nx.DiGraph()
  >
  > for i in range(len(tasks) - 1):
  >
  >    G.add_edge(tasks[i], tasks[i + 1])
  >
  > pos = nx.drawing.nx_pydot.graphviz_layout(G, prog="dot")
  >
  > plt.figure(figsize=(15, 8))
  >
  > nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
  >
  > plt.title("Workflow for Analyzing Urban Heat Using Kriging Interpolation", fontsize=14)
  >
  > plt.show()
  >
  >"""
  >
  >[Expected Sample Output End]

</details>

<details>
  <summary>Click to expand/collapse Code Generation Prompts</summary>

> As a Geospatial data scientist, generate a python file to solve the proposed task.
>
> [Task]:
> Identify hot spots for peak crashes
>
> [Instruction]:
> Your task is identifying hot spots for peak crashes in Brevard County, Florida, 2010 - 2015. The first
> step is select all the crashes based on peak time zone. Create a copy of selected crashes data. Then,
> snap the crashes points to the road network and spatial join with the road. Calculate the crash rate
> based on the joint data and use hot spot analysis to get crash hot spot map as the result.
>
> [Domain Knowledge]:
> We consider traffic between time zone 3pm to 5pm in weekdays as peak. For snap process, the recommend
> buffer on roads is 0.25 miles. Hot spot analysis looks for high crash rates that cluster close together,
> accurate distance measurements based on the road network are essential.
>
> [Dataset Description]:
> dataset/crashes.shp: The locations of crashes in Brevard County, Florida between 2010 and 2015.
>
> dataset/roads.shp: The road network of Brevard County.
>
> dataset/nwswm360ft.swm: Spatial weights matrix file created using the Generate Network Spatial
> Weights tool and a street network built from Brevard County road polylines.
>
> [Key Notes]:
> 1. Use **automatic reasoning** and clearly explain each subtask before performing it (ReAct approach).
>
> 2. Using latest python packages for code generation
>
> 3. Put all code under main function, no helper functions
>
> 4. Limit your output to code, no extra information.
>
> 5. Use latest **Arcpy** functions only
</details>

### Results

<p align="center">
  <img src="case_study/figures/TrafficAI.png" alt="traffic">
</p>

## Acknowledgement
We acknowledge the funding support from the National Science Foundation funded AI institute [Grant No. 2112606] for Intelligent Cyberinfrastructure with Computational Learning in the Environment (ICICLE). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funder(s). 
