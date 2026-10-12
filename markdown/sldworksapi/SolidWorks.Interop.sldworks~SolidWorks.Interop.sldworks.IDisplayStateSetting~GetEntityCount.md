---
title: "GetEntityCount Method (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "GetEntityCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetEntityCount.html"
---

# GetEntityCount Method (IDisplayStateSetting)

Gets the number of entities for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim value As System.Integer

value = instance.GetEntityCount()
```

### C#

```csharp
System.int GetEntityCount()
```

### C++/CLI

```cpp
System.int GetEntityCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities

## VBA Syntax

See [DisplayStateSetting::GetEntityCount](ms-its:sldworksapivb6.chm::/sldworks~DisplayStateSetting~GetEntityCount.html).

## Remarks

Call this method to get the size of the array returned by [IDisplayStateSetting::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~IGetEntities.html).

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)
[IDisplayStateSetting::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
