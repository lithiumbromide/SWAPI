---
title: "Faces Property (ISMNormalCutGroupData)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutGroupData"
member: "Faces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData~Faces.html"
---

# Faces Property (ISMNormalCutGroupData)

Gets or sets the cut-extrude faces in this group.

## Syntax

### Visual Basic (Declaration)

```vb
Property Faces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutGroupData
Dim value As System.Object

instance.Faces = value

value = instance.Faces
```

### C#

```csharp
System.object Faces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Faces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SMNormalCutGroupData::Faces](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutGroupData~Faces.html).

## Examples

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html) example.

## See Also

[ISMNormalCutGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.html)
[ISMNormalCutGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
