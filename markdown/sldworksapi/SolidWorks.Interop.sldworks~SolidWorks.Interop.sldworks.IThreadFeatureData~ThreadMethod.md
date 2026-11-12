---
title: "ThreadMethod Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "ThreadMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ThreadMethod.html"
---

# ThreadMethod Property (IThreadFeatureData)

Gets or sets the thread method for this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Integer

instance.ThreadMethod = value

value = instance.ThreadMethod
```

### C#

```csharp
System.int ThreadMethod {get; set;}
```

### C++/CLI

```cpp
property System.int ThreadMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread method as defined in [swThreadMethod_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadMethod_e.html); default is swThreadMethod_e.swThreadMethod_CutThread

## VBA Syntax

See [ThreadFeatureData::ThreadMethod](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~ThreadMethod.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
