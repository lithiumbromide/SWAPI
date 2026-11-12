---
title: "SplitPeriodicFaces Property (IMBDSTEP242Data)"
project: "SOLIDWORKS API Help"
interface: "IMBDSTEP242Data"
member: "SplitPeriodicFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~SplitPeriodicFaces.html"
---

# SplitPeriodicFaces Property (IMBDSTEP242Data)

Gets or sets whether to split periodic faces into two.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitPeriodicFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBDSTEP242Data
Dim value As System.Boolean

instance.SplitPeriodicFaces = value

value = instance.SplitPeriodicFaces
```

### C#

```csharp
System.bool SplitPeriodicFaces {get; set;}
```

### C++/CLI

```cpp
property System.bool SplitPeriodicFaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to split periodic faces, false to not

## VBA Syntax

See [MBDSTEP242Data::SplitPeriodicFaces](ms-its:sldworksapivb6.chm::/sldworks~MBDSTEP242Data~SplitPeriodicFaces.html).

## Examples

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html) examples.

## See Also

[IMBDSTEP242Data Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html)
[IMBDSTEP242Data Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
