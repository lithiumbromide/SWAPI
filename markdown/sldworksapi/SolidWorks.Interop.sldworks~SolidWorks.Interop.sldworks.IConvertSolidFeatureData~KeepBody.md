---
title: "KeepBody Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "KeepBody"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~KeepBody.html"
---

# KeepBody Property (IConvertSolidFeatureData)

Gets or sets whether to keep the original solid body when converting to sheet metal.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepBody As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean

instance.KeepBody = value

value = instance.KeepBody
```

### C#

```csharp
System.bool KeepBody {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepBody {
   System.bool get();
   void set (    System.bool value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to keep the original solid body, false to let the original body be consumed by the convert solid feature

## VBA Syntax

See

[ConvertSolidFeatureData::KeepBody](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~KeepBody.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
