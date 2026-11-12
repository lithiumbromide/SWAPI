---
title: "VariablePitch Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "VariablePitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.html"
---

# VariablePitch Property (IHelixFeatureData)

Gets whether this helix feature has a variable or constant pitch.

## Syntax

### Visual Basic (Declaration)

```vb
Property VariablePitch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Boolean

instance.VariablePitch = value

value = instance.VariablePitch
```

### C#

```csharp
System.bool VariablePitch {get; set;}
```

### C++/CLI

```cpp
property System.bool VariablePitch {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this helix feature has a variable pitch, false if this helix feature has a constant pitch

## VBA Syntax

See [HelixFeatureData::VariablePitch](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~VariablePitch.html).

## Examples

[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
