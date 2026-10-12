---
title: "FixProjectedLength Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "FixProjectedLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixProjectedLength.html"
---

# FixProjectedLength Property (IJogFeatureData)

Gets or sets whether to fix the projected length for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixProjectedLength As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Boolean

instance.FixProjectedLength = value

value = instance.FixProjectedLength
```

### C#

```csharp
System.bool FixProjectedLength {get; set;}
```

### C++/CLI

```cpp
property System.bool FixProjectedLength {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True fixes the projected length, false does not

## VBA Syntax

See [JogFeatureData::FixProjectedLength](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~FixProjectedLength.html).

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
