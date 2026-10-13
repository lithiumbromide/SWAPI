---
title: "Return Box Extents Example (C++ Dispatch)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Return_Box_Extents_Example_CPlusPlus_COM.htm"
---

# Return Box Extents Example (C++ Dispatch)

This example shows how to return the box extents of assembly components.

NOTE: There is no checking to see if the components are suppressed.

```vb
void GetComponentExtents()
{
 LPDISPATCH  pDispatch;
 IModelDoc  ModelDoc;
 IConfiguration Configuration;
 IComponent  RootComponent;
 VARIANT   varChildren;
 SafeArray*  psaChildren;
 VARIANT   varBox;
 SafeArray*  psaBox;
 IComponent  Child;
 long   i, nChildren;
 double   extent[6];
 double   value;
 long   j;

 // Get the AssemblyDoc
 pDispatch = GetSOLIDWORKS()->GetActiveDoc();
 ModelDoc.AttachDispatch(pDispatch);
 if ( ModelDoc.GetType() == swDocASSEMBLY )
 {

  // Get the direct children of this assembly
  if ( (pDispatch = ModelDoc.GetActiveConfiguration()) != NULL )
  {
   Configuration.AttachDispatch(pDispatch);

   if ( (pDispatch = Configuration.GetRootComponent()) != NULL )
   {
    RootComponent.AttachDispatch(pDispatch);

    varChildren = RootComponent.GetChildren();
    psaChildren = V_ARRAY(&varChildren);
    SafeArrayGetUBound(psaChildren, 1, &nChildren);
    for ( i=0; i<=nChildren; i++ )   // Note Ubound 0 is 1 child
    {
     SafeArrayGetElement(psaChildren, &i, &pDispatch);
     Child.AttachDispatch(pDispatch);

     // Extract the extents from the components
     varBox = Child.GetBox(FALSE, FALSE);
     psaBox = V_ARRAY(&varBox);
     SafeArrayLock(psaBox);
     for ( j=0; j<6; j++ )
     {
      SafeArrayGetElement(psaBox, &j, (VOID *)(&(value)));
      extent[j] = value;
     }

     // Destroy the Box SafeArray
     SafeArrayUnlock(psaBox);
     SafeArrayDestroy(psaBox);
     Child.ReleaseDispatch();
    }

    // Destroy the children SafeArray
    SafeArrayDestroy(psaChildren);
   }
  }
 }

 return;
}
```
