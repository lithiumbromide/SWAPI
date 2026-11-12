---
title: "SetPlaceInThisDrawing Method (IHyperLink)"
project: ""
interface: "IHyperLink"
member: "SetPlaceInThisDrawing"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHyperLink~SetPlaceInThisDrawing.html"
---

# SetPlaceInThisDrawing Method (IHyperLink)

Sets the hyperlink to a named location (e.g., Model, Sheet1, Sheet2, etc.) in the current drawing.

## Syntax

### Visual Basic

```vb
Sub SetPlaceInThisDrawing( _
   ByVal PlaceInDrawing As System.String _
)
```

### C#

```csharp
void SetPlaceInThisDrawing(
   System.string PlaceInDrawing
)
```

### JScript

```
function SetPlaceInThisDrawing(
   PlaceInDrawing : System.String
);
```

### Managed Extensions for C++

```
void SetPlaceInThisDrawing(
   System.string* PlaceInDrawing
)
```

### C++/CLI

```cpp
void SetPlaceInThisDrawing(
   System.String^ PlaceInDrawing
)
```

### Parameters

- `PlaceInDrawing`: Named location (e.g., **Model**,`filename`.**dwg**) for the hyperlink

## Remarks

This method is valid only if [IHyperLink::GetType](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetType.html) is dsHyperLinkType_e.dsHyperLinkType_PlaceInThisDrawing.

## See Also

[IHyperLink Interface](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)
[IHyperLink Members](Interop.dsAutomation~Interop.dsAutomation.IHyperLink_members.html)
[IHyperLink::GetAsPlaceInThisDrawing Method](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetAsPlaceInThisDrawing.html)

## Availability

DraftSight V1R1.3
