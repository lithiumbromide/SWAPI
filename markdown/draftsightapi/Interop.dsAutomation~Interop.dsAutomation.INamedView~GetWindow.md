---
title: "GetWindow Method (INamedView)"
project: ""
interface: "INamedView"
member: "GetWindow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INamedView~GetWindow.html"
---

# GetWindow Method (INamedView)

Gets the window that defines the named view.

## Syntax

### Visual Basic

```vb
Sub GetWindow( _
   ByRef FirstCorner As MathPoint, _
   ByRef OppositeCorner As MathPoint _
)
```

### C#

```csharp
void GetWindow(
   out MathPoint FirstCorner,
   out MathPoint OppositeCorner
)
```

### JScript

```
function GetWindow(
   FirstCorner : MathPoint,
   OppositeCorner : MathPoint
);
```

### Managed Extensions for C++

```
void GetWindow(
   [PARAMFLAG::Out] MathPoint* FirstCorner,
   [PARAMFLAG::Out] MathPoint* OppositeCorner
)
```

### C++/CLI

```cpp
void GetWindow(
   [Out] MathPoint^ FirstCorner,
   [Out] MathPoint^ OppositeCorner
)
```

### Parameters

- `FirstCorner`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of a corner of the window that defines the named view
- `OppositeCorner`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of a corner of the window, opposite FirstCorner, that defines the named view

## See Also

[INamedView Interface](Interop.dsAutomation~Interop.dsAutomation.INamedView.html)
[INamedView Members](Interop.dsAutomation~Interop.dsAutomation.INamedView_members.html)
[INamedView::SetWindow Method ()](Interop.dsAutomation~Interop.dsAutomation.INamedView~SetWindow.html)

## Availability

DraftSight V1R5.0
