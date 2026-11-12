---
title: "CreateCardView2 Method (IEdmFolder10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder10"
member: "CreateCardView2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder10~CreateCardView2.html"
---

# CreateCardView2 Method (IEdmFolder10)

Creates a data card view for the specified file or folder.

## Syntax

### Visual Basic

```vb
Function CreateCardView2( _
   ByVal lFileID As System.Integer, _
   ByVal lParentWindow As System.Integer, _
   ByVal lX As System.Integer, _
   ByVal lY As System.Integer, _
   Optional ByVal poCallback As EdmCallback, _
   Optional ByVal lEdmCardViewFlags As System.Integer _
) As IEdmCardView5
```

### C#

```csharp
IEdmCardView5 CreateCardView2(
   System.int lFileID,
   System.int lParentWindow,
   System.int lX,
   System.int lY,
   EdmCallback poCallback,
   System.int lEdmCardViewFlags
)
```

### C++/CLI

```cpp
IEdmCardView5^ CreateCardView2(
   System.int lFileID,
   System.int lParentWindow,
   System.int lX,
   System.int lY,
   EdmCallback^ poCallback,
   System.int lEdmCardViewFlags
)
```

### Parameters

- `lFileID`: ID of the file for which to create a data card view; 0 to create a view only for this folder
- `lParentWindow`: Handle of the window in which to create the data card view
- `lX`: X coordinate where to place the data card view relative to the upper-left corner of the window
- `lY`: Y coordinate where to place the data card view relative to the upper-left corner of the window
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to handle notifications from the data card view (see **Remarks**)
- `lEdmCardViewFlags`: Appearance and functionality of the data card view as defined in [EmdCardViewFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewFlag.html)

### Return Value

[IEdmCardView5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView5.html); Nothing or null if the file does not have a data card associated with it

## Examples

[Create Card View (C#)](Create_Card_View_Example_CSharp.htm)
[Create Card View (VB.NET)](Create_Card_View_Example_VBNET.htm)

## Remarks

If the callback is implemented for this card view:

- [IEdmCallback::SetModifiedFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback~SetModifiedFlag.html) is called whenever the user makes a change in the file data card.
- [IEdmCallback::SetProgressRange](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback~SetProgressRange.html) is called if the file data card contains a button connected to an add-in, and the add-in returns a combination of [EdmCardFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardFlag.html) values other than EdmCardFlag.EdmCF_Nothing. IEdmCallback::SetProgressRange is called with its lMin and lMax set to the EdmCardFlags passed in by the add-in. See [Calling VB.NET Add-ins](vbcardbutton.htm).

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmCardView5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The file does not have a card associated with it.

## See Also

[IEdmFolder10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder10.html)
[IEdmFolder10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder10_members.html)

## Availability

SOLIDWORKS PDM Professional 2017
