---
title: "GetID Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetID.html"
---

# GetID Method (ISheet)

Gets the ID of this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

ID of the drawing sheet

## VBA Syntax

See [Sheet::GetID](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetID.html).

## Examples

[Get ID of Active Configuration or Current Drawing Sheet (VB.NET)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VBNET.htm)
[Get ID of Active Configuration or Current Drawing Sheet (VBA)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VB.htm)
[Get ID of Active Configuration or Current Drawing Sheet (C#)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_CSharp.htm)

## Remarks

Each drawing sheet:

- is assigned a unique ID. This ID does not change if you change the name of the drawing sheet.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
