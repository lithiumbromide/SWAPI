---
title: "GetAsPlaceInThisDrawing Method (IHyperLink)"
project: ""
interface: "IHyperLink"
member: "GetAsPlaceInThisDrawing"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetAsPlaceInThisDrawing.html"
---

# GetAsPlaceInThisDrawing Method (IHyperLink)

Gets the hyperlink created for the specified named location (e.g., Model, Sheet1, Sheet2, etc.) in the drawing.

## Syntax

### Visual Basic

```vb
Function GetAsPlaceInThisDrawing( _
   ByRef PlaceInDrawing As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool GetAsPlaceInThisDrawing(
   out System.string PlaceInDrawing
)
```

### JScript

```
function GetAsPlaceInThisDrawing(
   PlaceInDrawing : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetAsPlaceInThisDrawing(
   [PARAMFLAG::Out] System.string* PlaceInDrawing
)
```

### C++/CLI

```cpp
System.bool GetAsPlaceInThisDrawing(
   [Out] System.String^ PlaceInDrawing
)
```

### Parameters

- `PlaceInDrawing`: Named location (e.g., **Model**,`filename`.**dwg**) for the hyperlink

### Return Value

True if successful, false if not

## Remarks

This method is valid only if [IHyperLink::GetType](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetType.html) is dsHyperLinkType_e.dsHyperLinkType_PlaceInThisDrawing.

## See Also

[IHyperLink Interface](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)
[IHyperLink Members](Interop.dsAutomation~Interop.dsAutomation.IHyperLink_members.html)
[IHyperLink::SetPlaceInThisDrawing Method](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~SetPlaceInThisDrawing.html)

## Availability

DraftSight V1R1.3
