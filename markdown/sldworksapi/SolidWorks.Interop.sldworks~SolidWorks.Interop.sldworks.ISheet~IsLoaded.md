---
title: "IsLoaded Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "IsLoaded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IsLoaded.html"
---

# IsLoaded Method (ISheet)

Gets whether this sheet is loaded.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsLoaded() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Boolean

value = instance.IsLoaded()
```

### C#

```csharp
System.bool IsLoaded()
```

### C++/CLI

```cpp
System.bool IsLoaded();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sheet is loaded, false if not

## VBA Syntax

See [Sheet::IsLoaded](ms-its:sldworksapivb6.chm::/sldworks~Sheet~IsLoaded.html).

## Examples

[Get Loaded Sheets (C#)](Get_Loaded_Sheets_Example_CSharp.htm)
[Get Loaded Sheets (VB.NET)](Get_Loaded_Sheets_Example_VBNET.htm)
[Get Loaded Sheets (VBA)](Get_Loaded_Sheets_Example_VB.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2009 SP3, Revision Number 17.3
