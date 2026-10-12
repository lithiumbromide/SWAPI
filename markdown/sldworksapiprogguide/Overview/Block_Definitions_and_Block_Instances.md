---
title: "Block Definitions and Block Instances"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Block_Definitions_and_Block_Instances.htm"
---

# Block Definitions and Block Instances

The [ISketchBlockDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchBlockDefinition.html) and [ISketchBlockInstance](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchBlockInstance.html) interfaces replace the now obsolete IBlockDefinition and IBlockInstance interfaces.

Blocks have definitions and instances. You can use block definitions and block instances in:

- parts and assemblies for laying out key design components in 2D, analyzing kinematic motion in 2D, analyzing tolerance stack-ups between mating parts or features, etc.
- drawings for items that you use often, such as standard notes, title blocks, label positions, etc.

In parts and assemblies only, block instances appear in the FeatureManager design tree under sketch features. In drawings only, block definitions appear as features in the FeatureManager design tree.

Edits to block definitions apply to all block instances of the same block definition, but changes to block instances apply only to the selected block instance.

The [ISketchManager](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchManager.html) interface includes methods for creating, inserting, getting, and editing block definitions and block instances.

### Block definitions

| To... | Use... | Instead of using the now obsolete... |
| --- | --- | --- |
| Create block definitions and compound notes | ISketchManager::MakeSketchBlockFromFile - or - ISketchManager::MakeSketchBlockFromSelected - or - ISketchManager::MakeSketchBlockFromSketch | IDrawingDoc::MakeBlockDefinition and IDrawingDoc::CreateCompoundNote |
| Edit block definitions | ISketchManager::EditSketchBlock and ISketchManager::EndEditSketchBlock | IDrawingDoc::GetEditBlock |
| Explode block definitions | ISketchManager::ExplodeSketchBlockInstance | IDrawingDoc::ExplodeBlockInstance |
| Get block definitions in parts or assemblies | ISketchManager::GetSketchBlockDefinitions - or - Traverse the FeatureManager design tree to get the sketch under which the block instance appears, get the block instance from the sketch using ISketch::GetSketchBlockInstances , and from the block instance get its block definition using ISketchBlockInstance::Definition | None |
| Get block definitions in drawings | ISketchManager::GetSketchBlockDefinitions - or - Traverse the FeatureManager design tree to get the block and then use IFeature::GetSpecificFeature2 | IDrawingDoc::GetBlockDefinition and IDrawingDoc::GetBlockDefinitions |
| Get notes in block definitions | ISketchBlockDefinition::GetNotes | IBlockDefinition::GetNotes |
| Get sketch and sketch entities in block definitions | ISketchBlockDefinition::GetArcs , ISketchBlockDefinition::GetEllipses , ISketchBlockDefinition::GetLines , ISketchBlockDefinition::GetParabolas , ISketchBlockDefinition::GetSketch , ISketchBlockDefinition::GetSplines2 , and ISketchBlockDefinition::GetUserPoints | IBlockDefinition::GetSketch |
| Identify sketch block definitions | ISketchBlockDefinition::GetFeature and IFeature::GetTypeName2 For example, in VBA: Dim swFeature as SldWorks.Feature Set swFeature = swSketchBlockDefinition. GetFeature Debug.Print swFeature. Name & [" & swFeature. GetTypeName2 & "]" swFeature.GetTypeName2 returns SketchBlockDef . | None |
| Link block definitions to files | ISketchBlockDefinition::FileName and ISketchBlockDefinition::LinkToFile | IBlockDefinition::GetExternalFileName, IBlockDefinition::GetUseExternalFile, IBlockDefinition::SetExternalFileName, and IBlockDefinition::SetUseExternalFile |
| Save block definitions to files | ISketchBlockDefinition::Save | IDrawingDoc::SaveBlock |

### Block instances

| To... | Use... | Instead of using the now obsolete... |
| --- | --- | --- |
| Edit block instances | ISketchBlockInstance::SetAttributeValue | IBlockInstance::SetAttributeValue |
| Explode block instances | ISketchManager::ExplodeSketchBlockInstance | IDrawingDoc::ExplodeBlockInstance |
| Get attributes and set attribute values for block instances | ISketchBlockInstance::GetAttributes , ISketchBlockInstance::GetAttributeValue , and ISketchBlockInstance::SetAttributeValue | IBlockInstance::GetAttributes, IBlockInstance::GetAttributeValue, and IBlockInstance::SetAttributeValue |
| Get block instances | ISketchBlockDefinition::GetInstances | IBlockDefinition::GetBlockInstances |
| Insert block instances | ISketchManager::InsertSketchBlockInstance | IDrawingDoc::InsertBlock - or - IBlockDefinition::InsertInstance |

Examine [ISketchManager](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchManager.html), [ISketchBlockDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchBlockDefinition.html), and [ISketchBlockInstance](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchBlockInstance.html) to see all of the methods and properties available for blocks. See the SOLIDWORKS Help for additional details about blocks.
