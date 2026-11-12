---
title: "Gap Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "Gap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~Gap.html"
---

# Gap Property (ICenterMark)

Gets or sets the gap between this center mark and extension line.

## Syntax

### Visual Basic (Declaration)

```vb
Property Gap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Double

instance.Gap = value

value = instance.Gap
```

### C#

```csharp
System.double Gap {get; set;}
```

### C++/CLI

```cpp
property System.double Gap {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gap

## VBA Syntax

See [CenterMark::Gap](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~Gap.html).

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
