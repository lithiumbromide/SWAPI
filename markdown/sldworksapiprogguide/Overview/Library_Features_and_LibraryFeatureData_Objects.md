---
title: "Library Features and LibraryFeatureData Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Library_Features_and_LibraryFeatureData_Objects.htm"
---

# Library Features and LibraryFeatureData Objects

#### To create a Library feature:

1. Use [IFeatureManager::CreateDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateDefinition.html) to create a new [LibraryFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILibraryFeatureData.html) object.
2. Initialize the library feature data object using [ILibraryFeatureData::Initialize](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILibraryFeatureData~Initialize.html) and a library feature.

  NOTE: This method initializes and opens the last active configuration.
3. If you do not want to apply the library feature to the last active configuration:
4. Set whether to link this library feature with the original library feature using [ILibraryFeatureData::LinkToLibraryPart](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILibraryFeatureData~LinktoLibraryPart.html).
5. Get the type of references required using [ILibraryFeatureData::GetReferences3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILibraryFeatureData~GetReferences3.html).
6. Get the locating dimension names and values using [ILibraryFeatureData::GetDimensions](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILibraryFeatureData~GetDimensions.html).
7. Select where to place the library feature using [IModelDocExtension::SelectByID2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~SelectByID2.html).
8. Create the library feature using [IFeatureManager::CreateFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateFeature.html).
