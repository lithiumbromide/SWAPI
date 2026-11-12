---
title: "IVertex Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "IVertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IVertex.html"
---

# IVertex Property (IWizardHoleFeatureData2)

Gets the end-condition vertex for the Hole Wizard feature.

****NOTE:** This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property IVertex As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As Vertex

instance.IVertex = value

value = instance.IVertex
```

### C#

```csharp
Vertex IVertex {get; set;}
```

### C++/CLI

```cpp
property Vertex^ IVertex {
   Vertex^ get();
   void set (    Vertex^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [WizardHoleFeatureData2::IVertex](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~IVertex.html).

## Remarks

To if end condition is to a vertex, use [IWizardHoleFeatureData2::SetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~SetEndConditionReference.html).

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Vertex.html)
[IWizardHoleFeatureData2::EndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~EndCondition.html)
[IWizardHoleFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetEndConditionReference.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
