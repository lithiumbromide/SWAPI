---
title: "GetNameCount Method (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "GetNameCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetNameCount.html"
---

# GetNameCount Method (IDisplayStateSetting)

Gets the number of display states for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNameCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim value As System.Integer

value = instance.GetNameCount()
```

### C#

```csharp
System.int GetNameCount()
```

### C++/CLI

```cpp
System.int GetNameCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DisplayStateSetting::GetNameCount](ms-its:sldworksapivb6.chm::/sldworks~DisplayStateSetting~GetNameCount.html).

## Remarks

Call this method to get the size of the array returned by [IDisplayStateSetting::IGetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~IGetNames.html).

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)
[IDisplayStateSetting::Names Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
