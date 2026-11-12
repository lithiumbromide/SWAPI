---
title: "IVertex Property (IWizardHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData"
member: "IVertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData~IVertex.html"
---

# IVertex Property (IWizardHoleFeatureData)

Obsolete. Superseded by [IWizardHoleFeatureData2::IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~IVertex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IVertex As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData
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

## VBA Syntax

See [WizardHoleFeatureData::IVertex](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData~IVertex.html).

## See Also

[IWizardHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData.html)
[IWizardHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData_members.html)
