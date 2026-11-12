---
title: "Getting Started"
project: "SOLIDWORKS Inspection API Help"
interface: ""
member: ""
kind: "topic"
source: "swinspectionapi/Getting Started.html"
---

# Getting Started

###### Activate SOLIDWORKS Inspection

To use the SOLIDWORKS Inspection add-in API, you must first:

- Install SOLIDWORKS Design Professional or Premium 2022 (or later).
- Install SOLIDWORKS Inspection 2022 (or later) with a valid license key.
- Activate the SOLIDWORKS Inspection add-in from SOLIDWORKS **Tools > Add-Ins...**.

After activation, you can access the user-interface help for SOLIDWORKS Inspection by selecting **Tools > SOLIDWORKS Inspection > Help and Quick Start Tour**. See how SOLIDWORKS Inspection works in the user interface before trying to balloon drawings using the SOLIDWORKS Inspection APIs.

###### How to balloon a drawing using the SOLIDWORKS Inspection APIs

1. Refer to the Examples in [IInspectionAddinMgr](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html).
2. Get the IInspectionMgr add-in object.
  Read [Accessing SOLIDWORKS Add-in Objects](ms-its:sldworksapiprogguide.chm:://Overview/Accessing_Add-ins.htm) to determine GUID or ProgID of the SOLIDWORKS Inspection add-in.

  For example in VBA,
  ...
  Dim inspectionMgr As SwInspectionAddin.InspectionAddinMgr
  Set progID = "Inspection.ExtSwAddin"
  Set inspectionMgr = SwApp.[GetAddInObject](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetAddInObject.html)(progID)
3. Create inspection project data.

  Dim projData As SwInspectionAddin.InspectionProjectData
  Set projData = inspectionMgr.[CreateInspectionProjectData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~CreateInspectionProjectData.html)
  'Specify properties in projData, e.g.,
  projData.[AutoBalloon](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~AutoBalloon.html) = True
  projData.[StartNumber](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~StartNumber.html) = 1
  projData.[IncludeNotes](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeNotes.html) = True
  projData.[NotesAutoExplode](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~NotesAutoExplode.html) = True
  projData.[Extraction](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~Extraction.html) = swiCharacteristicInfoExtraction_e.swiExtraction_Automatic
4. Balloon the drawing by creating an inspection project based on an inspection template and project data.
  Templates are located in `install_drive`**:\ProgramData\SOLIDWORKS\SolidWorks Inspection** `yyyy` **Addin\Templates**.

  Dim inspectionProj As SwInspectionAddin.InspectionProject
  Set inspectionProj = inspectionMgr.[CreateInspectionProject](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~CreateInspectionProject.html)("`dir_name\template_name`.swidot", projData)

###### How to modify the Bill of Characteristics

All of the inspection characteristics that you extracted during creation of the inspection project appear in a Bill of Characteristics.

**Modifying Characteristics**

After the model is ballooned, you can add/edit characteristics using:

inspectionMgr.[AddCharacteristics](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddCharacteristics.html)(annotationArray)

inspectionMgr.[GetCharacteristicIDs](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetCharacteristicIDs.html)

Set charData = inspectionMgr.[GetCharacteristicsData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetCharacteristicsData.html)(charID)

inspectionMgr.[EditCharacteristic](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~EditCharacteristic.html)(charID, charData)

**Exploding Characteristics**

You can separate characteristics into multiple instances whenever charData.[Quantity](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData~Quantity.html) >= 1 by setting:

projData.[CreateForEachInstance](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~CreateForEachInstance.html) = True

###### How to add/edit balloons

**Adding/Editing**

If you set projData.[AutoBalloon](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~AutoBalloon.html) to false, you can manually add inspection balloons.

Set aBalloonSettingsObject = inspectionMgr.[GetBalloonSettings](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetBalloonSettings.html)

'Specify the offsets and/or properties in the aBalloonSettingsObject.

Call inspectionMgr.[AddOrEditBalloons](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddOrEditBalloons.html)(aBalloonSettingsObject)

**Removing**

You can remove all balloons from the document.

Call inspectionMgr.[RemoveBalloons](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~RemoveBalloons.html)

**Selecting**

You can select all balloons in the document.

Call inspectionMgr.[SelectBalloons](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~SelectBalloons.html)

###### How to add customizations to the inspection report

Manage vendor, operation, and inspection method lists to fit company requirements by using:

- inspectionMgr.[GetVendors](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetVendors.html)
- inspectionMgr.[AddVendor](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddVendor.html)
- inspectionMgr.[DeleteVendors](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~DeleteVendors.html)
- inspectionMgr.[GetInspectionMethods](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetInspectionMethods.html)
- inspectionMgr.[AddInspectionMethod](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddInspectionMethod.html)
- inspectionMgr.[DeleteInspectionMethods](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~DeleteInspectionMethods.html)
- inspectionMgr.[GetOperations](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetOperations.html)
- inspectionMgr.[AddOperation](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddOperation.html)
- inspectionMgr.[DeleteOperations](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~DeleteOperations.html)

###### How to publish and export inspection reports using the SOLIDWORKS Inspection APIs

After you finish ballooning the drawing, you can export the inspection report in a variety of file types:

- inspectionProj.[ExportTo2DPDF](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject~ExportTo2DPDF.html)
- inspectionProj.[ExportTo3DPDF](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject~ExportTo3DPDF.html) (valid only for Parts)
- inspectionProj.[ExportToExcel](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject~ExportToExcel.html)
- inspectionProj.[ExportToEDrawings](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject~ExportToEDrawings.html)
