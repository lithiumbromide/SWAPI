---
title: "SetPrecision Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetPrecision"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision.html"
---

# SetPrecision Method (IDisplayDimension)

Obsolete. Superseded by [IDisplayDimension::SetPrecision2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetPrecision2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPrecision( _
   ByVal UseDoc As System.Boolean, _
   ByVal Primary As System.Integer, _
   ByVal Alternate As System.Integer, _
   ByVal PrimaryTol As System.Integer, _
   ByVal AlternateTol As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Primary As System.Integer
Dim Alternate As System.Integer
Dim PrimaryTol As System.Integer
Dim AlternateTol As System.Integer
Dim value As System.Integer

value = instance.SetPrecision(UseDoc, Primary, Alternate, PrimaryTol, AlternateTol)
```

### C#

```csharp
System.int SetPrecision(
   System.bool UseDoc,
   System.int Primary,
   System.int Alternate,
   System.int PrimaryTol,
   System.int AlternateTol
)
```

### C++/CLI

```cpp
System.int SetPrecision(
   System.bool UseDoc,
   System.int Primary,
   System.int Alternate,
   System.int PrimaryTol,
   System.int AlternateTol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`:
- `Primary`:
- `Alternate`:
- `PrimaryTol`:
- `AlternateTol`:

## VBA Syntax

See [DisplayDimension::SetPrecision](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetPrecision.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
