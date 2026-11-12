---
title: "DeleteAllCosmeticThreads Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "DeleteAllCosmeticThreads"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteAllCosmeticThreads.html"
---

# DeleteAllCosmeticThreads Method (IDrawingDoc)

Deletes all cosmetic threads, which do not have callouts, in a drawing of an assembly only.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteAllCosmeticThreads()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.DeleteAllCosmeticThreads()
```

### C#

```csharp
void DeleteAllCosmeticThreads()
```

### C++/CLI

```cpp
void DeleteAllCosmeticThreads();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::DeleteAllCosmeticThreads](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~DeleteAllCosmeticThreads.html).

## Examples

**VB.NET:**

'---------------------------------------------------

'

' Preconditions: Drawing of an assembly with

' cosmetic threads is active.

'

' Postconditions: Cosmetic threads without callouts

' are deleted.

'

'---------------------------------------------------

Option

Explicit On

Imports SOLIDWORKS.Interop.sldworks

Imports

SOLIDWORKS.Interop.swconst

Imports

System

Partial

Class SOLIDWORKSMacro

Public Sub main()

Dim swDrawingDoc As DrawingDoc

Dim swModel As ModelDoc2

Dim boolstatus As Boolean

swDrawingDoc = swApp.ActiveDoc

swDrawingDoc.DeleteAllCosmeticThreads()

swModel = swDrawingDoc

boolstatus = swModel.ForceRebuild3(False)

End Sub

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End

Class

## Remarks

This method only deletes cosmetic threads in a drawing of an assembly; this method does not delete cosmetic threads in a drawing of a part.

By default, cosmetic threads are not imported into an drawing of an assembly for performance reasons, but are imported into a drawing of part and belong to the features in the part; thus, they cannot be deleted using this method.

This method also does not delete any cosmetic threads with callouts in a drawing of an assembly.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
