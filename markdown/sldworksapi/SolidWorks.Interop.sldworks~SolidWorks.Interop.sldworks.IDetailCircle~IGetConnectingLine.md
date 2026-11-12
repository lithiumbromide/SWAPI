---
title: "IGetConnectingLine Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "IGetConnectingLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetConnectingLine.html"
---

# IGetConnectingLine Method (IDetailCircle)

Gets the end point coordinates of the connecting line

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConnectingLine() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Double

value = instance.IGetConnectingLine()
```

### C#

```csharp
System.double IGetConnectingLine()
```

### C++/CLI

```cpp
System.double IGetConnectingLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 6 doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IDetailCircle::GetConnectingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetConnectingLine.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
