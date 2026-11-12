---
title: "Hole Wizard Features andWizardHoleFeatureData2 Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Hole_Wizard_Features_and_WizardHoleFeatureData2_Objects.htm"
---

# Hole Wizard Features andWizardHoleFeatureData2 Objects

## Hole Wizard Features and WizardHoleFeatureData2 Objects

You can create a Hole Wizard feature by:

- Using an existing [WizardHoleFeatureData2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IWizardHoleFeatureData2.html) object.
- Creating a new IWizardHoleFeatureData2 object.

#### To create a Hole Wizard feature by using an existing hole wizard feature:

1. Select an existing hole wizard feature to get its IWizardHoleFeatureData2 object.
2. Use [IFeature::GetDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetDefinition.html) to get the IWizardHoleFeatureData2 object.
3. Select the reference entities to use to create the hole wizard feature.
4. Use [IFeatureManager::CreateFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateFeature.html) to create the new hole wizard feature.

#### To create a new Hole Wizard feature :

1. Use [IFeatureManager::CreateDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateDefinition.html) to create a new WizardHoleFeatureData2 object.
2. Initialize the feature data object using [IWizardHoleFeatureData2::InitializeHole.](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IWizardHoleFeatureDAta2~InitializeHole.html)
3. Change any default settings using the corresponding WizardHoleFeatureData2 properties.
4. Select the reference entities to use to create the hole wizard feature.
5. Use [IFeatureManager::CreateFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateFeature.html) to create the new hole wizard feature.
