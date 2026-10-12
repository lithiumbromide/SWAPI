---
title: "IGetComponents Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "IGetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetComponents.html"
---

# IGetComponents Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetComponents.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponents( _
   ByVal NCount As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim NCount As System.Integer
Dim value As Component2

value = instance.IGetComponents(NCount)
```

### C#

```csharp
Component2 IGetComponents(
   System.int NCount
)
```

### C++/CLI

```cpp
Component2^ IGetComponents(
   System.int NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of components in this hole series

### Return Value

- in-process, unmanaged C++: Pointer to an array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in this hole series

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IHoleSeriesFeatureData::GetComponentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData~GetComponentsCount.html) to get the value for NCount.

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponents.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
