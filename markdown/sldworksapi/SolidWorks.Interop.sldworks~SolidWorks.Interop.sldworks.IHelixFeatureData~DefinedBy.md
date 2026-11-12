---
title: "DefinedBy Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "DefinedBy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DefinedBy.html"
---

# DefinedBy Property (IHelixFeatureData)

Gets or sets the definition of this helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefinedBy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Integer

instance.DefinedBy = value

value = instance.DefinedBy
```

### C#

```csharp
System.int DefinedBy {get; set;}
```

### C++/CLI

```cpp
property System.int DefinedBy {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of helix as defined by [swHelixDefinedBy_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHelixDefinedBy_e.html)

## VBA Syntax

See [HelixFeatureData::DefinedBy](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~DefinedBy.html).

## Examples

[Create or Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create or Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create or Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
