---
title: "Label Property (IPMIDatumFeature)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumFeature"
member: "Label"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature~Label.html"
---

# Label Property (IPMIDatumFeature)

Gets the non-numeric label of this PMI datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Label As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumFeature
Dim value As System.String

instance.Label = value

value = instance.Label
```

### C#

```csharp
System.string Label {get; set;}
```

### C++/CLI

```cpp
property System.String^ Label {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Datum label

## VBA Syntax

See [PMIDatumFeature::Label](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumFeature~Label.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.html)
[IPMIDatumFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
