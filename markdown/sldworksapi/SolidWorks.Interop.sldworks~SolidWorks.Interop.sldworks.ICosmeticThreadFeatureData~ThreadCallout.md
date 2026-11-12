---
title: "ThreadCallout Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "ThreadCallout"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~ThreadCallout.html"
---

# ThreadCallout Property (ICosmeticThreadFeatureData)

Gets or sets the callout text for this cosmetic thread feature in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadCallout As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.String

instance.ThreadCallout = value

value = instance.ThreadCallout
```

### C#

```csharp
System.string ThreadCallout {get; set;}
```

### C++/CLI

```cpp
property System.String^ ThreadCallout {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Callout text for this cosmetic thread feature in a drawing

## VBA Syntax

See [CosmeticThreadFeatureData::ThreadCallout](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~ThreadCallout.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
