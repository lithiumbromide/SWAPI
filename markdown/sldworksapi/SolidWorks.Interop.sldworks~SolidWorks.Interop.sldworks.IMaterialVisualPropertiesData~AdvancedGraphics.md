---
title: "AdvancedGraphics Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "AdvancedGraphics"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~AdvancedGraphics.html"
---

# AdvancedGraphics Property (IMaterialVisualPropertiesData)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Property AdvancedGraphics As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean

instance.AdvancedGraphics = value

value = instance.AdvancedGraphics
```

### C#

```csharp
System.bool AdvancedGraphics {get; set;}
```

### C++/CLI

```cpp
property System.bool AdvancedGraphics {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the part is displayed with shaded textures, false if not

## VBA Syntax

See [MaterialVisualPropertiesData::AdvancedGraphics](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~AdvancedGraphics.html).

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)
[IMaterialVisualPropertiesData::RealView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~RealView.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
