---
title: "NumberOfStarts Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "NumberOfStarts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~NumberOfStarts.html"
---

# NumberOfStarts Property (IThreadFeatureData)

Gets or sets the number of times the thread is created in an evenly-spaced pattern around the hole or shaft of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfStarts As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Integer

instance.NumberOfStarts = value

value = instance.NumberOfStarts
```

### C#

```csharp
System.int NumberOfStarts {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfStarts {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

2 (default) <= Number of times the thread is started <= 1000

## VBA Syntax

See [ThreadFeatureData::NumberOfStarts](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~NumberOfStarts.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if [IThreadFeatureData::MultipleStart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.html) is set to true.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
