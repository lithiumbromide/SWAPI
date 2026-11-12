---
title: "GetPTZHeight Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetPTZHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight.html"
---

# GetPTZHeight Method (IGtol)

Obsolete. Superseded by [IGtol::GetPTZHeight2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPTZHeight() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.String

value = instance.GetPTZHeight()
```

### C#

```csharp
System.string GetPTZHeight()
```

### C++/CLI

```cpp
System.String^ GetPTZHeight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Height of the projected tolerance zone (see **Remarks**)

## VBA Syntax

See [Gtol::GetPTZHeight](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetPTZHeight.html).

## Remarks

This method returns the height of the projected tolerance zone as a string because it is a user-specified parameter that can be textual, numeric, or both types of data.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::SetPTZHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight.html)
