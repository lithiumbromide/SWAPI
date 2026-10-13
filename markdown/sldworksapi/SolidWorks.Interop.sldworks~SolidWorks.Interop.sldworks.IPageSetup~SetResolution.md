---
title: "SetResolution Method (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "SetResolution"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetResolution.html"
---

# SetResolution Method (IPageSetup)

Sets the current printer resolution on documents and drawing sheets.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResolution( _
   ByVal UseDefault As System.Boolean, _
   ByVal DPI As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim UseDefault As System.Boolean
Dim DPI As System.Integer
Dim value As System.Boolean

value = instance.SetResolution(UseDefault, DPI)
```

### C#

```csharp
System.bool SetResolution(
   System.bool UseDefault,
   System.int DPI
)
```

### C++/CLI

```cpp
System.bool SetResolution(
   System.bool UseDefault,
   System.int DPI
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDefault`: True to use the default printer resolution, false to set the printer resolution
- `DPI`: Dots per inch

### Return Value

True if printer resolution is set, false if not

## VBA Syntax

See [PageSetup::SetResolution](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~SetResolution.html).

## Remarks

Specifying IPageSetup::SetResolution (false, 0) turns on the default resolution, which results in [IPageSetup::GetUseDefaultResolution](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~GetUseDefaultResolution.html) returning True.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetResolution.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
