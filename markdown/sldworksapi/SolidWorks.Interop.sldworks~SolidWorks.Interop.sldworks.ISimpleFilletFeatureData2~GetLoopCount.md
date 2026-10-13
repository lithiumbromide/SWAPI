---
title: "GetLoopCount Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetLoopCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetLoopCount.html"
---

# GetLoopCount Method (ISimpleFilletFeatureData2)

Gets the number of loops on which to create a single radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoopCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

value = instance.GetLoopCount()
```

### C#

```csharp
System.int GetLoopCount()
```

### C++/CLI

```cpp
System.int GetLoopCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of loops

## VBA Syntax

See [SimpleFilletFeatureData2::GetLoopCount](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetLoopCount.html).

## Remarks

Call this method before calling [ISimpleFilletFeatureData2::IGetLoops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetLoops.html) to get the size of the array for that method.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetLoops.html)
[ISimpleFilletFeatureData2::Loops Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Loops.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
