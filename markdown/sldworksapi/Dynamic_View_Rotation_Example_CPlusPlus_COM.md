---
title: "Dynamic View Rotation Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Dynamic_View_Rotation_Example_CPlusPlus_COM.htm"
---

# Dynamic View Rotation Example (C++ COM)

## Dynamically Rotate Model View Example (C++ COM)

This example shows how to dynamically rotate a model view. It also shows you how to speed up the process by using the StartDynamics and StopDynamics calls.

```vb
RotateTheView(ISldWorks* m_pSldWorks)
{
 LPMODELDOC2 p_ModelDoc = NULL;
 LPMODELVIEW p_ModelView = NULL;
 HRESULT res = S_OK;
 // Retrieve the model document pointer
 res = m_pSldWorks->get_IActiveDoc2( &p_ModelDoc );
 if( res != S_OK || p_ModelDoc == NULL )
  return;
  // Get the active view pointer
 res = p_ModelDoc->get_IActiveView(&p_ModelView);
 if( res != S_OK || p_ModelView == NULL )
 {
  p_ModelDoc->Release();
  return;
 }
 int i;
 // Prepare view for rotation
 p_ModelView->StartDynamics();
 for (i = 1; i < 100; i++)
 {
   p_ModelDoc->ViewRotateplusy();
 }
 // End dynamic rotation mode
 p_ModelView->StopDynamics();
 // Repaint the screen
 p_ModelDoc->GraphicsRedraw2();
 //Clean up
 p_ModelView->Release();
 p_ModelDoc->Release();
}
```
