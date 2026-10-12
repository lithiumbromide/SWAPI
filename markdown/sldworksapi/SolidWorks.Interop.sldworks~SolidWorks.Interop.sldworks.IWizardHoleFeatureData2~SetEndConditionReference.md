---
title: "SetEndConditionReference Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "SetEndConditionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~SetEndConditionReference.html"
---

# SetEndConditionReference Method (IWizardHoleFeatureData2)

Sets the reference entity that defines the end condition for this Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEndConditionReference( _
   ByVal PDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim PDisp As System.Object

instance.SetEndConditionReference(PDisp)
```

### C#

```csharp
void SetEndConditionReference(
   System.object PDisp
)
```

### C++/CLI

```cpp
void SetEndConditionReference(
   System.Object^ PDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDisp`: Reference entity that defines the end condition

## VBA Syntax

See [WizardHoleFeatureData2::SetEndConditionReference](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~SetEndConditionReference.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetEndConditionReference.html)
[IWizardHoleFeatureData2::EndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~EndCondition.html)
[IWizardHoleFeatureData2::Face Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Face.html)
[IWizardHoleFeatureData2::IFace Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IFace.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
