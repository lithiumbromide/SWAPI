---
title: "Text Property (IPMIDatumFeature)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumFeature"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature~Text.html"
---

# Text Property (IPMIDatumFeature)

Gets the PMI datum text.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Text As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumFeature
Dim value As System.String

instance.Text = value

value = instance.Text
```

### C#

```csharp
System.string Text {get; set;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

PMI datum text

## VBA Syntax

See [PMIDatumFeature::Text](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumFeature~Text.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.html)
[IPMIDatumFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
