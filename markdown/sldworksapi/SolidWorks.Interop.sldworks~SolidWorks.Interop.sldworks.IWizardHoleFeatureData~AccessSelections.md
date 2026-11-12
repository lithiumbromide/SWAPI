---
title: "AccessSelections Method (IWizardHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData~AccessSelections.html"
---

# AccessSelections Method (IWizardHoleFeatureData)

Obsolete. Superseded by [IWizardHoleFeatureData2::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~AccessSelections.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean

value = instance.AccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool AccessSelections(
   System.object TopDoc,
   System.object Component
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   System.Object^ TopDoc,
   System.Object^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`:
- `Component`:

## VBA Syntax

See [WizardHoleFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData~AccessSelections.html).

## See Also

[IWizardHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData.html)
[IWizardHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData_members.html)
