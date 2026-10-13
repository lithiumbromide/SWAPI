---
title: "GetConnectingLine Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetConnectingLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetConnectingLine.html"
---

# GetConnectingLine Method (IDetailCircle)

Gets the end point coordinates of the connecting line for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectingLine() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Object

value = instance.GetConnectingLine()
```

### C#

```csharp
System.object GetConnectingLine()
```

### C++/CLI

```cpp
System.Object^ GetConnectingLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [DetailCircle::GetConnectingLine](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetConnectingLine.html).

## Remarks

This is only valid if there is a connecting line. Use [IDetailCircle::GetStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~GetStyle.html) to determine if this detail circle is valid for this command.

| retval[0] | X-coordinate of first connecting line point |
| --- | --- |
| retval[1] | Y-coordinate of first connecting line point |
| retval[2] | Z-coordinate of first connecting line point |
| retval[3] | X-coordinate of second connecting line point |
| retval[4] | Y-coordinate of second connecting line point |
| retval[5] | Z-coordinate of second connecting line point |

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::IGetConnectingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetConnectingLine.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
