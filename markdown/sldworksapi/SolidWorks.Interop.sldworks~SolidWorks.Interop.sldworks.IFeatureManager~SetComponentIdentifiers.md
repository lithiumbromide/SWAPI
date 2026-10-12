---
title: "SetComponentIdentifiers Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "SetComponentIdentifiers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetComponentIdentifiers.html"
---

# SetComponentIdentifiers Method (IFeatureManager)

Allows you to specify the primary, ( secondary ), and < tertiary > elements to display for the components in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponentIdentifiers( _
   ByVal Primary As System.Integer, _
   ByVal Secondary As System.Integer, _
   ByVal Tertiary As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Primary As System.Integer
Dim Secondary As System.Integer
Dim Tertiary As System.Integer
Dim value As System.Integer

value = instance.SetComponentIdentifiers(Primary, Secondary, Tertiary)
```

### C#

```csharp
System.int SetComponentIdentifiers(
   System.int Primary,
   System.int Secondary,
   System.int Tertiary
)
```

### C++/CLI

```cpp
System.int SetComponentIdentifiers(
   System.int Primary,
   System.int Secondary,
   System.int Tertiary
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Primary`: Component identifier as defined by [swComponentIdentifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentIdentifier_e.html)
- `Secondary`: Component identifier(s) as defined by swComponentIdentifier_e
- `Tertiary`: Component identifier(s) as defined by swComponentIdentifier_e

### Return Value

Result code as defined by [swSetComponentIdentifierResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetComponentIdentifierResult_e.html)

## VBA Syntax

See [FeatureManager::SetComponentIdentifiers](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~SetComponentIdentifiers.html).

## Examples

'VBA

'-------------------------------------------------------
' Preconditions:
' 1. Open `public_documents`**\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\smartcomponents\pillow_block.sldasm**.
' 2. Widen the FeatureManager design tree.
'
' Postconditions: Inspect the FeatureManager design tree and press F5 after each Stop.
'
' Notes: Because the model is used elsewhere, do not save changes.
'-------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim swFeatMgr As SldWorks.FeatureManager
Dim compIdentifierRet As Long

Sub main()
Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc
Set swFeatMgr = Part.FeatureManager

' Do show configuration or display state name if only one exists
swFeatMgr.**HideComponentSingleConfigurationOrDisplayStateNames** = False

' Set primary identifier
compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier_ComponentName, 0, 0)
Stop

compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier_ComponentDescription, 0, 0)
Stop

' Set primary and secondary identifiers
compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier_ComponentName, swComponentIdentifier_ConfigurationName, 0)
Stop

compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier_ComponentName, swComponentIdentifier_ConfigurationDescription, 0)
Stop

compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier_ComponentName, swComponentIdentifier_ComponentDescription, 0)
Stop

'Set primary, secondary, and tertiary identifiers
compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier_ComponentName, swComponentIdentifier_ConfigurationName + swComponentIdentifier_ConfigurationDescription + swComponentIdentifier_ComponentDescription, swComponentIdentifier_DisplayStateName)
Stop

End Sub

## Remarks

This method:

- Works in both SOLIDWORKS Design and [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).
- Is analogous to right-clicking on the top-level component in the FeatureManager design tree and selecting **Tree Display > Component Name and Description**.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ComponentPrimaryIdentifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentPrimaryIdentifier.html)
[IFeatureManager::ComponentSecondaryIdentifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentSecondaryIdentifier.html)
[IFeatureManager::ComponentTertiaryIdentifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentTertiaryIdentifier.html)

## Availability

SOLIDWORKS 2022 SP01, Revision Number 30.1
