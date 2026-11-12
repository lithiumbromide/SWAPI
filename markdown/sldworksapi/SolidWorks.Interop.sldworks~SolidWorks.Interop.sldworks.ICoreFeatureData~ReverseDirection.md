---
title: "ReverseDirection Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (ICoreFeatureData)

Gets or sets the direction of the extraction for this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction, false to not

## VBA Syntax

See [CoreFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~ReverseDirection.html).

## Examples

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
