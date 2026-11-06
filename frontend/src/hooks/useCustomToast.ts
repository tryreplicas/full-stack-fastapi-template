import { toast } from "sonner"

const useCustomToast = () => {
  const notifySuccess = (description: string) => {
    toast.success("Success!", {
      description,
    })
  }

  const notifyError = (description: string) => {
    toast.error("Something went wrong!", {
      description,
    })
  }

  return { notifySuccess, notifyError }
}

export default useCustomToast
