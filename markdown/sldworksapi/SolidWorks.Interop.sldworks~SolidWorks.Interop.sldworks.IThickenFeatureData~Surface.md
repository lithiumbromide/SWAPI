---
title: "Surface Property (IThickenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData"
member: "Surface"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~Surface.html"
---

# Surface Property (IThickenFeatureData)

Gets or sets the thickened surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property Surface As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IThickenFeatureData
Dim value As System.Object

instance.Surface = value

value = instance.Surface
```

### C#

```csharp
System.object Surface {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Surface {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thickened surface, which is an [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

## VBA Syntax

See [ThickenFeatureData::Surface](ms-its:sldworksapivb6.chm::/sldworks~ThickenFeatureData~Surface.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
