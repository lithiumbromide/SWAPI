---
title: "IGetNames Method (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "IGetNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetNames.html"
---

# IGetNames Method (IDisplayStateSetting)

Gets the display state names for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNames( _
   ByVal DsNameCount As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim DsNameCount As System.Integer
Dim value As System.String

value = instance.IGetNames(DsNameCount)
```

### C#

```csharp
System.string IGetNames(
   System.int DsNameCount
)
```

### C++/CLI

```cpp
System.String^ IGetNames(
   System.int DsNameCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DsNameCount`: Number of display state names

### Return Value

- in-process, unmanaged C++: Pointer to an array display state names
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IDisplayStateSetting::GetNameCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~GetNameCount.html) to populate DsNameCount.

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)
[IDisplayStateSetting::Names Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.html)
[IDisplayStateSetting::ISetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
