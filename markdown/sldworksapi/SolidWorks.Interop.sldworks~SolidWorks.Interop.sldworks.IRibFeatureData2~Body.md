---
title: "Body Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "Body"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~Body.html"
---

# Body Property (IRibFeatureData2)

Gets or sets the body where the rib is created.

## Syntax

### Visual Basic (Declaration)

```vb
Property Body As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As Body2

instance.Body = value

value = instance.Body
```

### C#

```csharp
Body2 Body {get; set;}
```

### C++/CLI

```cpp
property Body2^ Body {
   Body2^ get();
   void set (    Body2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) where rib is created

## VBA Syntax

See [RibFeatureData2::Body](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~Body.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
