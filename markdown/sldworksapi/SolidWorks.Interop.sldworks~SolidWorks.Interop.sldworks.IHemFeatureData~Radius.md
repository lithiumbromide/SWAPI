---
title: "Radius Property (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "Radius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~Radius.html"
---

# Radius Property (IHemFeatureData)

Gets or sets the hem radius for tear drop and rolled hems only.

## Syntax

### Visual Basic (Declaration)

```vb
Property Radius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
Dim value As System.Double

instance.Radius = value

value = instance.Radius
```

### C#

```csharp
System.double Radius {get; set;}
```

### C++/CLI

```cpp
property System.double Radius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hem radius

## VBA Syntax

See [HemFeatureData::Radius](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~Radius.html).

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
